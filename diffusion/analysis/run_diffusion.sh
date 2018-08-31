# Run MSD code for a list of numpy arrays in the same directory
diff_code='/home/kutay/Documents/git/lammps_tools/bin/npytraj_diffusivity.py'
np_array_dir='/home/kutay/Documents/git/Nanocar/diffusion/docs/pos_np_array/temperature-rigid/DC_Cu110'
plot_dir='/home/kutay/Documents/git/Nanocar/diffusion/docs/diff_plots/temperature-rigid/DC_Cu110'

cd $np_array_dir
for i in `ls`
do

echo '-------------------------------------'
echo 'SIM:' $i
echo '-------------------------------------'
python $diff_code $i --fs-per-row 1000 --output-molecule-plots --all-fits
mkdir $plot_dir/$i
mv *.png $plot_dir/$i/.
mv fit_results.yaml $plot_dir/$i/.

done
