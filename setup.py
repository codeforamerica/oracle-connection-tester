from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = dict(
    packages=['decimal'],
    excludes=[],
    include_files=['config.json.sample', 'launch.bat']
)

bdist_msi_options = dict(
    upgrade_code="{7d6b167a-29b4-11e6-84de-b8e856155eba}"
)

base = 'Console'

executables = [
    Executable('run_connection_test.py', base=base)
]

setup(
    name='comport-connection-test',
    version='0.1.1',
    description='Tests connection to an Oracle database.',
    options=dict(build_exe=build_options, bdist_msi=bdist_msi_options),
    executables=executables
)
