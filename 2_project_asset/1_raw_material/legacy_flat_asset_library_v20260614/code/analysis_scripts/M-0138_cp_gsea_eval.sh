#!/bin/bash
#SBATCH -J cp_gsea
#SBATCH -N 1
#SBATCH -p normal
#SBATCH -n 8
#SBATCH -o /public/home/caojun/project/RUSH/3_work/report/log.out/cp_gsea.out
#SBATCH -e /public/home/caojun/project/RUSH/3_work/report/log.out/cp_gsea.err
#SBATCH --mem=96G
data_id=$1  
echo pseudo $data_id
/public/home/caojun/anaconda3/envs/crane_test/bin/python \
/public/home/caojun/project/RUSH/3_work/script/cp_gsea_eval.py $data_id
echo 'data_id is ok'
 