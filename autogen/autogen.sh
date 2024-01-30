#!/bin/bash

SCRIPT_DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUT_DIR="$( cd -P "$( dirname "${SCRIPT_DIR}" )" && pwd )"

if [ ! -d "${SCRIPT_DIR}/foreman" ]; then
  echo 'The foreman directory has not been created yet.'
  exit 1
fi

if [ ! -f "${SCRIPT_DIR}/foreman/schema_swagger_form_data.en.json" ]; then
  echo 'The swagger schema file cannot be found in the foreman directory.'
  exit 1
fi

pushd "$OUT_DIR" >/dev/null || exit 1

docker run --rm -it \
  -v "${OUT_DIR}":/local \
  swaggerapi/swagger-codegen-cli \
  generate \
  -c /local/autogen/pyforeman.json \
  -l python \
  --git-repo-base-url https://github.com \
  --git-repo-id foreman-python-client \
  --git-user-id broadinstitute \
  -i /local/autogen/foreman/schema_swagger_form_data.en.json \
  -o "/local"

cat autogen/swagger-codegen-ignore >> "${OUT_DIR}/.gitignore"
rm -f "${OUT_DIR}/.travis.yml"

docker run -it --rm \
  -v "${OUT_DIR}":/local \
  --workdir /local \
  pyfound/black:latest_release \
  black '/local'

pre-commit run end-of-file-fixer -a
pre-commit run trailing-whitespace -a

popd >/dev/null || exit 1
