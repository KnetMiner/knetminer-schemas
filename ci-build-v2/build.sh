#!/usr/bin/env bash
set -e

function stage_build_setup_local
{
	printf "== Installing Python environment and requirements\n"
	python -m venv pyenv
	. ./pyenv/bin/activate

	pip install -r requirements.txt
}



function stage_build_local
{
	build_semantic-motif-taxonomy	
}

function build_semantic-motif-taxonomy
{
	printf "=== Processing Semantic Motif Taxonomy\n"
	cd semantic-motif-taxonomy

	printf "== Validation\n"
	linkml lint knet-motif-categories.linkml.yaml

	printf "\n== Markdown Docs\n"
	doc_dir=knet-motif-categories-doc
	rm -Rf "$doc_dir"
	linkml generate doc --hierarchical-class-view --directory "$doc_dir" \
	  knet-motif-categories.linkml.yaml

	git add "$doc_dir"

	cd ..
	printf "\n=== /end: Processing Semantic Motif Taxonomy\n"
}


function stage_deploy_local
{
	stage_deploy
	is_deploy_mode || return 0

	printf "== Updating local changes to git\n"

	if ! $(git status --porcelain); then
		printf "= No changes happened in the build (same files commited?), skipping git update"
		return 0
	fi

	git commit -a -m "Updating auto-generated files from CI $CI_SKIP_TAG"
	export CI_NEEDS_PUSH=true
}



function install_and_import 
{
	url_base="$1"
	printf "\n== Downloading from URL base '%s'\n\n" "$url_base"

	file_local_paths=("_common.sh")

	# Relative to the <git root>/ci-build-v2
	for file_local_path in "${file_local_paths[@]}"
	do
		file_local_path="ci-build-v2/$file_local_path"
		[[ ! -e "$file_local_path" ]] || continue;
				
		url="$url_base/${file_local_path}"
		file_path="$(realpath "${file_local_path}")"		
		dir_path="$(dirname "${file_path}")"
		
		printf "= Downloading '%s' to '%s'" "$url" "${file_path}\n"

		mkdir -p "${dir_path}"
		curl --fail-with-body "$url" -o "${file_path}"
	done

	# Eventually, these should be here.
	. ./ci-build-v2/_common.sh	

	# WARNING: the best way to override functions defined in these imported files is 
	# doing it in your own definition file and then importing it after the original ones, like
	# it's shown here.
	# This is not necessary if you only have stage_xxx_local() functions (or only your own new
	# functions).
	#
	# . ./ci-build-v2/_common-local.sh
}

install_and_import "https://raw.githubusercontent.com/Rothamsted/knetminer-common/refs/heads/ci-build-v2"
main
