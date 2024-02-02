#Author: Jay Annadurai
#Date: 2 Feb 2024
#Title: A1 - DES (Download, Extract, Summarize)
#Desc: Unix Bash Script to Download, Extract, and Summarize Chromosome Assemblies into a Text File

#1. Navigate to the user’s home directory

#Change Directory to the Parent Directory for the upcoming Informatics Folder
echo "Changing Directory to /Home"
cd "/home"

#NOTE, MUST USE THIS TO TEST ON MAC
#cd "/Users/jannadurai/desktop"
#echo "Changing Directory to User's Desktop

#2. Create a directory titled “Informatics_573” and navigate to it

#Create the specified 'Informatics_573' directory or utilize it if it already exists [-p] and then shift into it only if it succeeds
echo "Making 'Informatics_573' Directory"
mkdir -p "Informatics_573" && cd "Informatics_573"

#3. Download all secondary assemblies for human chromosome 1 from University of California, Santa Cruz (UCSC) Genome browser (all chromosome 1 assemblies except “chr1.fa.gz”)

#Using wget to download files from the UCSC Genome Browser
#https://hgdownload.soe.ucsc.edu/goldenPath/currentGenomes/Homo_sapiens/chromosomes/
echo "Downloading Chromosome 1 Assemblies from UCSC Genome Browser"
#Needs option to download all the chr1 files
#Note all the desired chr1 files look like char1_***.fa.gz
# -r to overwrite and -nc to keep 'no clobber'
wget -nc --accept="chr1_*.fa.gz" "ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/*"

#4. Unzip all of the downloaded chromosome 1 assemblies
# Loop through all the chromosome assemblies
for zipfile in *.fa.gz; do
    #Unzip the file
    gunzip $zipfile
    #Echo a message indicating that the file has been unzipped
    echo $zipfile "unzipped!"
done

#5. Create a new empty file called “data_summary.txt”
logfile="data_summary.txt"
touch $logfile

#6. Append a list of the all detailed information (including at least file name, size, and permissions) to “data_summary.txt”
# Loop through all assembly files
for assemblyFile in *.fa; do

    #Build a Divider
    div="-----------------------------------------------------"
    
    #Get the Base Name of the Assembly File by Removing the '.fa' extension and getting the Base Name and then take that entire output and store as a variable
    assemblyFileName=$(basename $assemblyFile .fa)
    #echo "$assemblyFileName"

    #Get the File Size in Bytes
    assemblyFileSizeBytes=$(wc -c < "$assemblyFile")
    #echo "$assemblyFileSizeBytes"

    #Get the Assembly File Permissions

    #Uses awk to print the first (permissions), third (owner), and fourth (group) fields from the output of ls -l.
    assemblyFilePermissions=$(ls -l "$assemblyFile" | awk '{print $1, $3, $4}')
    #echo "$assemblyFilePermissions" 

    #7. Append the first 10 lines of each of the chromosome 1 assemblies to “data_summary.txt”

    #First 10 Lines of Each AssemblyFile
    #To skip the chromosome name, and just get the first 10 lines
    #First get the entire document skipping the first 2 lines and then pipe that into the head with a specification for the first 10 lines (note default is 10 anyways)
    assemblyFileFirst10Lines=$(tail -n +2 "$assemblyFile" | head -n 10)
    #assemblyFileFirst10Lines=$(head -n +1 "$assemblyFile")
    #echo "$assemblyFileFirst10Lines"

    #8. Append the name of assembly as well as the total number of lines included in that assembly to “data_summary.txt”

    #Get the Chromosome Name (Same as Filename)
    assemblyName=$(head -n 1 "$assemblyFile")
    #echo "$assemblyFileName"

    #Get the File Size in Lines
    assemblyFileSizeLines=$(wc -l < "$assemblyFile")
    #echo "$assemblyFileSizeLines"


    #Echo all the Data in a formatted Manner and Pipe the Data to the Log File
    echo "$div" >> "$logfile"
    echo "$assemblyFileName" >> "$logfile"
    echo "$div" >> "$logfile"
    echo "Size (B):  $assemblyFileSizeBytes" >> "$logfile"
    echo "Lines:     $assemblyFileSizeLines" >> "$logfile"
    echo "Perms: $assemblyFilePermissions" >> "$logfile"
    echo "$div" >> "$logfile"
    echo "Chr Assembly $assemblyName First 10 Lines:" >> "$logfile"
    echo "$assemblyFileFirst10Lines" >> "$logfile"
    echo "$div" >> "$logfile"
    echo "" >> "$logfile"
    echo "" >> "$logfile"

    #Log Completion of the Data Summary for Each Secondary Chromosome Assembly to the Terminal
    echo "Completed Data Summary for: $assemblyName"

done





