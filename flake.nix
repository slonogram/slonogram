{
  description = "flake for `slonogram` library";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = import nixpkgs { inherit system; };
            python = pkgs.python311;

            base-pkgs = [
              python
            ] ++ (with pkgs; [
              uv
              just
            ]);
        in
          {
            devShells.default = pkgs.mkShell {
              buildInputs = base-pkgs ++ (with pkgs; [
                ruff
              ]);
            };
          }
      );
}
