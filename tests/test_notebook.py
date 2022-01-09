import os
import subprocess
import tempfile

import nbformat


def run_notebook(filename):
    """
    Execute the specified notebook via jupyter nbconvert and collect output.
    :returns (parsed nb object, execution errors)
    """
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # get temporary file ( and then close to avoid multiple write problems
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        temp_name = fout.name

    # run jupyter nbconvert
    args = ["jupyter", "nbconvert", "--to", "notebook", filename, "--execute",
            "--ExecutePreprocessor.timeout=60", "--output", temp_name]
    # subprocess.check_call(args, shell=True)
    subprocess.run(args)

    # read and parse notebook
    with open(filename, 'r+', encoding="utf-8") as fout:
        fout.seek(0)
        notebook = nbformat.read(fout, nbformat.current_nbformat)

    errors = [output for cell in notebook.cells if "outputs" in cell
              for output in cell["outputs"] \
              if output.output_type == "error"]

    return notebook, errors

# This will work, but only if all libraries are in your default python environment.
def test_notebook():
   notebook, errors = run_notebook('notebooks//2.0_user_segmentation.ipynb')
   assert errors == []
