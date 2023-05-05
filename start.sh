

# conda list -e > req.txt
# conda create -n <environment-name> --file req.txt

envname=bmlnav

# if this environment doesn't exist, create one with req.txt
if conda info --envs | grep -q $envname; then echo "$envname already exists"; else conda create -n $envname --file req.txt; fi

conda activate bmlnav

python bmlnav.py