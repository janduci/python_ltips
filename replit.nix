{pkgs}: {
  deps = [
    pkgs.python312Packages.ipython
    pkgs.iproute2
    pkgs.dig
    pkgs.nettools
    pkgs.vim
  ];
}
