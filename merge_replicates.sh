echo "Create output folder."
mkdir output


for prefix in $(ls *R1* | awk -F- '{print $1"-"$2"-"$3}' | uniq) ; do

  echo Merging...
      
  ls *$prefix*R1*fastq.gz | tr " " "\n"

  ls *$prefix*R1*fastq.gz | xargs cat > output/${prefix}_R1.fastq.gz

  echo Saved to output/${prefix}_R1.fastq.gz

  echo "----"

  echo Merging...

  ls *$prefix*R2*fastq.gz | tr " " "\n"

  ls *$prefix*R2*fastq.gz | xargs cat > output/${prefix}_R2.fastq.gz

  echo Saved to output/${prefix}_R2.fastq.gz

done

echo "Finished"
