
echo "Create output folder."
mkdir output 
for prefix in $(ls *L00*.fastq.gz | xargs -I {} echo {} | sed 's/_L00/$/' | cut -d "$" -f1 | uniq); do 

   echo ""

   echo Merging...    
   ls  ${prefix}_*_R1* | tr " " "\n"
   ls ${prefix}_*_R1* | xargs cat > output/${prefix}_R1.fastq.gz
   echo Saved to output/${prefix}_R1.fastq.gz

   echo ""

   echo Merging...
   ls  ${prefix}_*_R2* | tr " " "\n"    
   ls ${prefix}_*_R2* | xargs cat > output/${prefix}_R2.fastq.gz
   echo Saved to output/${prefix}_R2.fastq.gz

done 

echo "Finished" 

sleep 3d
