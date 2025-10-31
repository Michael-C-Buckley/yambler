{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python
    python313
    uv
    ruff
    gcc
    pkg-config

    # Pre-commit
    lefthook
    typos
    bandit
  ];
  env = {
    LD_LIBRARY_PATH = with pkgs; lib.makeLibraryPath [stdenv.cc.cc];
    LC_ALL = "C.UTF-8";
    LOCALE_ARCHIVE = "${pkgs.glibcLocales}/lib/locale/locale-archive";
    UV_LINK_MODE = "copy";
    UV_PROJECT_ENVIRONMENT = "$VIRTUAL_ENV";
  };
}
