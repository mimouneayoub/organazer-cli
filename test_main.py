from click.testing import CliRunner

from main import main


def test_organize_by_ext():
    runner = CliRunner()


    result = runner.invoke(main,['organize-by-ext','.', '--extention','txt'])

    assert result.exit_code == 0


