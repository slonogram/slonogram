{
  description = "slonogram";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem(system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = {
          pkg = pkgs.python311;
          packages = pkgs.python311Packages;
        };
      in
      {
        devShells.default = pkgs.mkShell {
          shellHook = ''
            export PS1="<slonogram> $PS1"
          '';
          buildInputs = [ python.pkg ] ++ (with python.packages; [
            python-lsp-server
            mypy
            pylsp-mypy
            python-lsp-ruff
          ]) ++ (with pkgs; [
            uv
            ruff
            nickel
          ]);
        };
      }
    );
}
