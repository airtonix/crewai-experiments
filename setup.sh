#!/usr/bin/env bash

# Local vars
ASDF_VERSION=${ASDF_VERSION:-v0.14.0}
ASDF_HOME=$HOME/.asdf
ASDF_BIN=$ASDF_HOME/asdf.sh

set -e

require() {
  if ! command -v "$1" &>/dev/null; then
    echo "📛📦 Missing $1"
    exit 1
  fi
}

append_uniquely() {
  if ! grep -q "$2" "$1"; then
    echo "====> ✍ Writing \"$2\" into \"$1\" "
    echo "${2}" >>"$1"
  fi
}

get_shell_profile() {
  case "${SHELL}" in
  /bin/bash)
    echo ~/.bashrc
    return 0
    ;;
  /bin/zsh)
    echo ~/.zshrc
    return 0
    ;;
  esac
}

install_asdf() {
  local has_asdf_directory
  local has_asdf_bin

  has_asdf_directory=$(test -d "$ASDF_HOME" && echo "true")
  has_asdf_bin=$(test -f "$ASDF_BIN" && echo "true")

  # if there's no asdf directory or binary, install it
  if [ "$has_asdf_directory" != "true" ] || [ "$has_asdf_bin" != "true" ]; then
    echo "===> ⤵️ ASDF not detected ... installing"
    git clone https://github.com/asdf-vm/asdf.git "$ASDF_HOME" --branch "$ASDF_VERSION"

    # if asdf is not on the path, add it and refresh the shell
    require asdf || {
      echo "====> ⚕️ adding to shell profile"
      append_uniquely "$(get_shell_profile)" ". $ASDF_HOME/asdf.sh"
      append_uniquely "$(get_shell_profile)" ". $ASDF_HOME/completions/asdf.bash"
    }
  fi

  # shellcheck source=/dev/null
  source "$ASDF_BIN"

  asdf update
}

install_deps() {
  asdf plugin add asdf-plugin-manager https://github.com/asdf-community/asdf-plugin-manager.git
  asdf plugin update asdf-plugin-manager v1.2.0
  asdf install asdf-plugin-manager 1.2.0
  asdf global asdf-plugin-manager 1.2.0
  asdf reshim
  asdf-plugin-manager add-all

  echo "==> 💁 [ASDF] install tools"
  asdf install

  echo "==> 💁 [ASDF] reshim binaries"
  asdf reshim

  echo "==> 💁 [ASDF] Done ✅"
}

require git
require curl

install_asdf
install_deps
