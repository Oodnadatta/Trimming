#! /bin/sh

#Anne-Sophie Denommé-Pichon
#AGPLv3

for fastq in /work/gad/shared/analyse/STR/Data/*fastq.gz
do
    dijen="$(basename "$fastq" | sed 's#\(dijen[0-9]\+\)\.R[1-2]\.fastq\.gz#\1#')"
    end_name="$(basename "$fastq" | sed 's#dijen[0-9]\+\(\.R[1-2]\.fastq\.gz\)#\1#')"
    for i in 75 100
    do
	gunzip -c "$fastq" | /user1/gad/an1770de/Scripts/trimming/fastq_trimming.py "$i" | gzip -1 > "/work/gad/shared/analyse/STR/Data/$dijen/${dijen}_trimming_$i${end_name}"
    done &
done
