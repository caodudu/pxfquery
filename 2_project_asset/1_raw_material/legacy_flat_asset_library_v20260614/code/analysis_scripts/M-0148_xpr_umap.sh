#!/bin/bash
#SBATCH -J xpr_umap
#SBATCH -N 1
#SBATCH -p normal
#SBATCH -n 8
#SBATCH -o /public/home/caojun/project/RUSH/3_work/report/log.out/xpr_umap.out
#SBATCH -e /public/home/caojun/project/RUSH/3_work/report/log.out/xpr_umap.err
#SBATCH --mem=96G
 
/public/home/caojun/anaconda3/envs/crane_test/bin/python \
/public/home/caojun/project/RUSH/3_work/script/umap/xpr_umap.py  
 