pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

blueprints = custom_target('blueprints',
  input: files(
    'window.blp'
),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('sortpictureresolve-gui',
  'sortpictureresolve-gui.gresource.xml',
  gresource_bundle: true,
  dependencies: blueprints,
  install: true,
  install_dir: pkgdatadir,
)