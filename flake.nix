{
  description = "flake for `slonogram` library";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs = {
        nixpkgs.follows = "nixpkgs";
        flake-utils.follows = "nixpkgs";
      };
    };
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    poetry2nix,
    ...
  }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = import nixpkgs { inherit system; };
            python = pkgs.python311;

            base-pkgs = [
              python
              pkgs.poetry
              pkgs.just
            ];
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
