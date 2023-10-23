#!/usr/bin/env sh

Argument="$1"  # Pass the variable as a command-line argument

Argument=${Argument//\\//}

echo "$Argument"  # Output the modified variable
