pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

gnome.compile_resources('sortpictureresolve-gui',
  'sortpictureresolve-gui.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)