#!/usr/bin/env bash
main () {
	if (( $# != 2 )); then
		echo "Usage: $0 <string1> <string2>"
		return 1
	fi
	if (( "${#1}" != "${#2}" )); then
		echo "left and right strands must be of equal length"
		return 1
	fi
	p=0
	for (( l=0; l<${#1}; l++ )); do
		if [[ "${1:l:1}" != "${2:l:1}" ]]; then
			(( ++p ))
		fi
	done
	echo "$p"
}
main "$@"
