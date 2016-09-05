<h1>
 Awesome Bioinformatics
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<blockquote>
 <p>
  Bioinformatics is an interdisciplinary field that develops methods and software tools for understanding biological data. —
  <a href="https://en.wikipedia.org/wiki/Bioinformatics">
   Wikipedia
  </a>
 </p>
</blockquote>
<p>
 A curated list of awesome Bioinformatics software, resources, and libraries. Mostly command line based, and free or open-source. Please feel free to
 <a href="CONTRIBUTING.md">
  contribute
 </a>
 !
</p>
<p>
 <strong>
  Table of Contents
 </strong>
</p>
<p>
 <!-- START doctoc generated TOC please keep comment here to allow auto update -->
 <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
</p>
<ul>
 <li>
  <a href="#data-processing">
   Data Processing
  </a>
  <ul>
   <li>
    <a href="#command-line-utilities">
     Command Line Utilities
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#next-generation-sequencing">
   Next Generation Sequencing
  </a>
  <ul>
   <li>
    <a href="#pipelinespipeline-frameworks">
     Pipelines/Pipeline frameworks
    </a>
   </li>
   <li>
    <a href="#sequence-processing">
     Sequence Processing
    </a>
   </li>
   <li>
    <a href="#sequence-alignment">
     Sequence Alignment
    </a>
   </li>
   <li>
    <a href="#variant-calling">
     Variant Calling
    </a>
   </li>
   <li>
    <a href="#bam-file-utilities">
     BAM File Utilities
    </a>
   </li>
   <li>
    <a href="#vcf-file-utilities">
     VCF File Utilities
    </a>
   </li>
   <li>
    <a href="#genomic-traits">
     Genomic Traits
    </a>
   </li>
   <li>
    <a href="#variant-simulation">
     Variant Simulation
    </a>
   </li>
   <li>
    <a href="#variant-filtering--quality-control">
     Variant Filtering / Quality Control
    </a>
   </li>
   <li>
    <a href="#variant-predictionannotation">
     Variant Prediction/Annotation
    </a>
   </li>
   <li>
    <a href="#python-modules">
     Python Modules
    </a>
   </li>
   <li>
    <a href="#data">
     Data
    </a>
   </li>
   <li>
    <a href="#tools">
     Tools
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#visualization">
   Visualization
  </a>
  <ul>
   <li>
    <a href="#genome-browsers--gene-diagrams">
     Genome Browsers / Gene diagrams
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#database-access">
   Database Access
  </a>
 </li>
 <li>
  <a href="#resources">
   Resources
  </a>
  <ul>
   <li>
    <a href="#becoming-a-bioinformatician">
     Becoming a Bioinformatician
    </a>
   </li>
   <li>
    <a href="#sequencing">
     Sequencing
    </a>
   </li>
   <li>
    <a href="#rna-seq">
     RNA-Seq
    </a>
   </li>
   <li>
    <a href="#chip-seq">
     ChIP-Seq
    </a>
   </li>
   <li>
    <a href="#youtube-channels-and-playlists">
     YouTube Channels and Playlists
    </a>
   </li>
   <li>
    <a href="#blogs">
     Blogs
    </a>
   </li>
   <li>
    <a href="#miscellaneous">
     Miscellaneous
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="#license">
   License
  </a>
 </li>
</ul>
<p>
 <!-- END doctoc generated TOC please keep comment here to allow auto update -->
</p>
<hr/>
<h2>
 Data Processing
</h2>
<h3>
 Command Line Utilities
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.gnu.org/software/datamash/">
    datamash
   </a>
  </strong>
  - Data transformations and statistics.
 </li>
 <li>
  <strong>
   <a href="https://github.com/stephenturner/oneliners">
    Bioinformatics One Liners
   </a>
  </strong>
  - Git repo of useful single line commands.
 </li>
 <li>
  <strong>
   <a href="https://github.com/arq5x/bedtools2">
    Bedtools2
   </a>
  </strong>
  - A Swiss Army knife for genome arithmetic.
 </li>
 <li>
  <strong>
   <a href="https://github.com/onyxfish/csvkit">
    CSVKit
   </a>
  </strong>
  - Utilities for working with CSV/Tab-delimited files.
 </li>
 <li>
  <strong>
   <a href="https://github.com/shenwei356/csvtk">
    csvtk
   </a>
  </strong>
  - Another cross-platform, efficient, practical and pretty CSV/TSV toolkit.
 </li>
 <li>
  <strong>
   <a href="https://github.com/shenwei356/easy_qsub">
    easy_qsub
   </a>
  </strong>
  - Easily submitting PBS jobs with script template. Multiple input files supported.
 </li>
 <li>
  <strong>
   <a href="http://www.gnu.org/software/parallel/">
    GNU
    <code>
     parallel
    </code>
   </a>
  </strong>
  - General parallelizer that runs jobs in parallel on a single multi-core machine.
  <a href="https://www.biostars.org/p/63816/">
   Here
  </a>
  are some example scripts using GNU
  <code>
   parallel
  </code>
  .
 </li>
</ul>
<h2>
 Next Generation Sequencing
</h2>
<h3>
 Pipelines/Pipeline frameworks
</h3>
<ul>
 <li>
  <strong>
   <a href="http://www.ruffus.org.uk">
    Ruffus
   </a>
  </strong>
  - Computation Pipeline library for python widely used in science and bioinformatics.
 </li>
 <li>
  <strong>
   <a href="https://bitbucket.org/snakemake/snakemake/wiki/Home">
    Snakemake
   </a>
  </strong>
  - A workflow management system in Python that aims to reduce the complexity of creating workflows by providing a fast and comfortable execution environment.
 </li>
 <li>
  <strong>
   <a href="https://www.nextflow.io">
    Nextflow
   </a>
  </strong>
  - A fluent DSL modelled around the UNIX pipe concept, that simplifies writing parallel and scalable pipelines in a portable manner.
 </li>
 <li>
  <strong>
   <a href="https://pcingola.github.io/BigDataScript">
    BigDataScript
   </a>
  </strong>
  - A cross-system scripting language for working with big data pipelines in computer systems of different sizes and capabilities.
 </li>
 <li>
  <strong>
   <a href="http://docs.bpipe.org">
    Bpipe
   </a>
  </strong>
  - A small language for defining pipeline stages and linking them together to make pipelines.
 </li>
 <li>
  <strong>
   <a href="http://gatkforums.broadinstitute.org/firecloud/discussion/1306/overview-of-queue">
    GATK Queue
   </a>
  </strong>
  - A pipelining system built to work natively with GATK as well as other high-throughput sequence analysis software.
 </li>
 <li>
  <strong>
   <a href="https://seqware.github.io/">
    SeqWare
   </a>
  </strong>
  - Hadoop Oozie-based workflow system focused on genomics data analysis in cloud environments.
 </li>
 <li>
  <strong>
   <a href="https://github.com/chapmanb/bcbio-nextgen">
    bcbio-nextgen
   </a>
  </strong>
  - Batteries included genomic analysis pipeline for variant and RNA-Seq analysis, structural variant calling, annotation, and prediction.
  <sup>
   &#9733 297, pushed 126 days ago
  </sup>
 </li>
</ul>
<h3>
 Sequence Processing
</h3>
<p>
 Sequence Processing includes tasks such as demultiplexing raw read data, and trimming low quality bases.
</p>
<ul>
 <li>
  <strong>
   <a href="https://github.com/shenwei356/fakit">
    fakit
   </a>
  </strong>
  - A cross-platform and efficient toolkit for FASTA/Q file manipulation.
 </li>
 <li>
  <strong>
   <a href="https://github.com/mdshw5/fastqp">
    Fastqp
   </a>
  </strong>
  - Fastq and Sam quality control using python.
 </li>
 <li>
  <strong>
   <a href="http://www.bioinformatics.babraham.ac.uk/projects/fastqc/">
    FastQC
   </a>
  </strong>
  - A quality control tool for high throughput sequence data.
 </li>
 <li>
  <strong>
   <a href="http://hannonlab.cshl.edu/fastx_toolkit/">
    Fastx Tookit
   </a>
  </strong>
  - FASTQ/A short-reads pre-processing tools: Demultiplexing, trimming, clipping, quality filtering, and masking utilities.
 </li>
 <li>
  <strong>
   <a href="https://github.com/lh3/seqtk">
    Seqtk
   </a>
  </strong>
  - Toolkit for processing sequences in FASTA/Q formats.
 </li>
</ul>
<h3>
 Sequence Alignment
</h3>
<p>
 <strong>
  De Novo Alignment
 </strong>
</p>
<p>
 <strong>
  DNA Resequencing
 </strong>
</p>
<ul>
 <li>
  <strong>
   <a href="https://github.com/lh3/bwa">
    BWA
   </a>
  </strong>
  Burrow-Wheeler Aligner for pairwise alignment between DNA sequences.
 </li>
</ul>
<h3>
 Variant Calling
</h3>
<ul>
 <li>
  <strong>
   <a href="https://github.com/samtools/samtools">
    samtools/bcftools/htslib
   </a>
  </strong>
  - A suite of tools for manipulating next-generation sequencing data.
 </li>
 <li>
  <strong>
   <a href="https://github.com/ekg/freebayes">
    freebayes
   </a>
  </strong>
  - Bayesian haplotype-based polymorphism discovery and genotyping.
 </li>
</ul>
<h3>
 BAM File Utilities
</h3>
<ul>
 <li>
  <a href="https://github.com/pezmaster31/bamtools">
   Bamtools
  </a>
  - Collection of tools for working with BAM files.
 </li>
</ul>
<h3>
 VCF File Utilities
</h3>
<ul>
 <li>
  <strong>
   <a href="https://github.com/ekg/vcflib">
    vcflib
   </a>
  </strong>
  - A C++ library for parsing and manipulating VCF files.
 </li>
 <li>
  <strong>
   <a href="https://github.com/samtools/bcftools">
    bcftools
   </a>
  </strong>
  - Set of tools for manipulating VCF files.
 </li>
 <li>
  <strong>
   <a href="http://vcftools.sourceforge.net/">
    vcftools
   </a>
  </strong>
  - VCF manipulation and statistics (e.g. linkage disequilibrium, allele frequency, Fst).
 </li>
</ul>
<h4>
 Genomic Traits
</h4>
<p>
 <strong>
  Genomic Traits
 </strong>
 are differences in terms of DNA structure or content observed among populations that may be regulated by genetic variation. For example, telomere length or rDNA copy number.
</p>
<ul>
 <li>
  <strong>
   <a href="https://github.com/zd1/telseq">
    Telseq
   </a>
  </strong>
  - Telseq is a tool for estimating telomere length from whole genome sequence data.
 </li>
 <li>
  <strong>
   <a href="https://github.com/AndersenLab/bam-toolbox">
    bam toolbox
   </a>
  </strong>
  MtDNA:Nuclear Coverage; Bam Toolbox can output the ratio of MtDNA:nuclear coverage, a proxy for mitochondrial content.
 </li>
</ul>
<h3>
 Variant Simulation
</h3>
<ul>
 <li>
  <strong>
   <a href="https://github.com/lh3/wgsim">
    wgsim
   </a>
  </strong>
  -
  <strong>
   Comes with samtools!
  </strong>
  - Reads simulator.
 </li>
 <li>
  <strong>
   <a href="https://github.com/adamewing/bamsurgeon">
    Bam Surgeon
   </a>
  </strong>
  - Tools for adding mutations to existing .bam files, used for testing mutation callers.
 </li>
</ul>
<h3>
 Variant Filtering / Quality Control
</h3>
<h3>
 Variant Prediction/Annotation
</h3>
<ul>
 <li>
  <strong>
   <a href="http://sift.jcvi.org/">
    SIFT
   </a>
  </strong>
  - Predicts whether an amino acid substitution affects protein function.
 </li>
 <li>
  <strong>
   <a href="http://snpeff.sourceforge.net/">
    SnpEff
   </a>
  </strong>
  - Genetic variant annotation and effect prediction toolbox.
 </li>
</ul>
<h3>
 Python Modules
</h3>
<h4>
 Data
</h4>
<ul>
 <li>
  <strong>
   <a href="https://github.com/brentp/cruzdb">
    cruzdb
   </a>
  </strong>
  - Pythonic access to the UCSC Genome database.
 </li>
 <li>
  <strong>
   <a href="https://github.com/hammerlab/pyensembl">
    pyensembl
   </a>
  </strong>
  - Pythonic Access to the Ensembl database.
 </li>
</ul>
<h4>
 Tools
</h4>
<ul>
 <li>
  <strong>
   <a href="https://github.com/mdshw5/pyfaidx">
    pyfaidx
   </a>
  </strong>
  - Pythonic access to FASTA files.
 </li>
 <li>
  <strong>
   <a href="https://github.com/daler/pybedtools">
    pyBedTools
   </a>
  </strong>
  - Python wrapper for
  <a href="https://github.com/arq5x/bedtools">
   bedtools
  </a>
  .
 </li>
 <li>
  <strong>
   <a href="https://github.com/pysam-developers/pysam">
    pysam
   </a>
  </strong>
  - Python wrapper for
  <a href="https://github.com/samtools/samtools">
   samtools
  </a>
  .
 </li>
 <li>
  <strong>
   <a href="https://github.com/jamescasbon/PyVCF">
    pyVCF
   </a>
  </strong>
  - A VCF Parser for python.
 </li>
 <li>
  <strong>
   <a href="https://github.com/arq5x/cyvcf">
    cyvcf
   </a>
  </strong>
  - A port of
  <a href="https://github.com/jamescasbon/PyVCF">
   pyVCF
  </a>
  using Cython for speed.
 </li>
 <li>
  <strong>
   <a href="https://github.com/brentp/cyvcf2">
    cyvcf2
   </a>
  </strong>
  - cython + htslib == fast VCF parsing; Even faster parsing than pyVCF.
 </li>
</ul>
<h2>
 Visualization
</h2>
<h3>
 Genome Browsers / Gene diagrams
</h3>
<p>
 The following tools can be used to visualize genomic data or for constructing customized visualizations of genomic data including sequence data from DNA-Seq, RNA-Seq, and ChIP-Seq, variants, and more.
</p>
<ul>
 <li>
  <strong>
   <a href="http://www.biodalliance.org/">
    biodalliance
   </a>
  </strong>
  - Embeddable genome viewer. Integration data from a wide variety of sources, and can load data directly from popular genomics file formats including bigWig, BAM, and VCF.
 </li>
 <li>
  <strong>
   <a href="https://www.broadinstitute.org/igv/">
    IGV js
   </a>
  </strong>
  - Java based browser. Fast, efficient, scalable visualization tool for genomics data and annotations. Handles a large
  <a href="http://www.broadinstitute.org/igv/FileFormats">
   variety of formats
  </a>
  .
 </li>
 <li>
  <strong>
   <a href="https://github.com/lairdm/islandplot">
    Island Plot
   </a>
  </strong>
  - D3 JavaScript based genome viewer. Constructs SVGs.
 </li>
 <li>
  <strong>
   <a href="https://github.com/hammerlab/pileup.js">
    pileup.js
   </a>
  </strong>
  - JavaScript library that can be used to generate interactive and highly customizable web-based genome browsers.
 </li>
 <li>
  <strong>
   <a href="https://github.com/chmille4/Scribl">
    scribl
   </a>
  </strong>
  - JavaScript library for drawing canvas-based gene diagrams. The
  <a href="http://chmille4.github.io/Scribl/">
   Homepage
  </a>
  has examples.
 </li>
 <li>
  <strong>
   <a href="https://github.com/drio/dnaism">
    DNAism
   </a>
  </strong>
  - Horizon chart d3-based js library for DNA data.
 </li>
</ul>
<h2>
 Database Access
</h2>
<ul>
 <li>
  <a href="http://www.ncbi.nlm.nih.gov/books/NBK179288/">
   Entrez Direct: E-utilities on the UNIX command line
  </a>
  - UNIX command line tools to access NCBI's databases programmatically. Instructions to install and examples are found in the link.
 </li>
</ul>
<h2>
 Resources
</h2>
<h3>
 Becoming a Bioinformatician
</h3>
<ul>
 <li>
  <a href="http://blog.fejes.ca/?p=2418">
   What is a bioinformatician
  </a>
 </li>
 <li>
  <a href="http://www.ploscompbiol.org/article/info:doi%2F10.1371%2Fjournal.pcbi.1003496">
   Bioinformatics Curriculum Guidelines: Toward a Definition of Core Competencies
  </a>
 </li>
 <li>
  <a href="http://caseybergman.wordpress.com/2012/07/31/top-n-reasons-to-do-a-ph-d-or-post-doc-in-bioinformaticscomputational-biology/">
   Top N Reasons To Do A Ph.D. or Post-Doc in Bioinformatics/Computational Biology
  </a>
 </li>
 <li>
  <a href="http://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-1-104">
   A 10-Step Guide to Party Conversation For Bioinformaticians
  </a>
  - Here is a step-by-step guide on how to convey concepts to people not involved in the field when asked the question: 'So, what do you do?'
 </li>
 <li>
  <a href="http://video.open-bio.org/video/1/a-history-of-bioinformatics-in-the-year-2039">
   A History Of Bioinformatics (In The Year 2039)
  </a>
  - A talk by C. Titus Brown on his take of looking back at bioinformatics from the year 2039. His notes for this talk can be found
  <a href="http://ivory.idyll.org/blog/2014-bosc-keynote.html">
   here
  </a>
  .
 </li>
 <li>
  <a href="http://madhadron.com/posts/2012-03-26-a-farewell-to-bioinformatics.html">
   A farewell to bioinformatics
  </a>
  - A critical view of the state of bioinformatics.
 </li>
 <li>
  <a href="http://www.acgt.me/blog/2014/3/25/101-questions-a-new-series-of-interviews-with-notable-bioinformaticians">
   A Series of Interviews with Notable Bioinformaticians
  </a>
  - Dr. Keith Bradnam "thought it might be instructive to ask a simple series of questions to a bunch of notable bioinformaticians to assess their feelings on the current state of bioinformatics research, and maybe get any tips they have about what has been useful to their bioinformatics careers."
 </li>
 <li>
  <a href="https://gitlab.com/genomic/learning-resources">
   Learning Resources Index
  </a>
  -
  <a href="https://gitlab.com/u/Adrianzo">
   Adrián E. Salatino's
  </a>
  attempt at consolidating useful links and resources he has found helpful in his graduate career, ranging from (but not limited to) programming help, bioinformatics software, and even blogs to follow.
 </li>
</ul>
<h3>
 Sequencing
</h3>
<ul>
 <li>
  <a href="https://youtu.be/6Is3W7JkFp8">
   Next-Generation Sequencing Technologies - Elaine Mardis (2014)
  </a>
  [1:34:35] - Excellent (technical) overview of next-generation and third-generation sequencing technologies, along with some applications in cancer research.
 </li>
 <li>
  <a href="https://liorpachter.wordpress.com/seq/">
   Annotated bibliography of *Seq assays
  </a>
  - List of ~100 papers on various sequencing technologies and assays ranging from transcription to transposable element discovery.
 </li>
 <li>
  <a href="http://www.illumina.com/content/dam/illumina-marketing/documents/applications/ngs-library-prep/ForAllYouSeqMethods.pdf">
   For all you seq... (PDF)
  </a>
  (3456x5471) - Massive infographic by Illumina on illustrating how many sequencing techniques work. Techniques cover protein-protein interactions, RNA transcription, RNA-protein interactions, RNA low-level detection, RNA modifications, RNA structure, DNA rearrangements and markers, DNA low-level detection, epigenetics, and DNA-protein interactions. References included.
 </li>
</ul>
<h3>
 RNA-Seq
</h3>
<ul>
 <li>
  <a href="https://www.biostars.org/p/52152/">
   Review papers on RNA-seq (Biostars)
  </a>
  - Includes lots of seminal papers on RNA-seq and analysis methods.
 </li>
 <li>
  <a href="https://github.com/griffithlab/rnaseq_tutorial">
   Informatics for RNA-seq: A web resource for analysis on the cloud
  </a>
  - Educational resource on performing RNA-seq analysis in the cloud using Amazon AWS cloud services. Topics include preparing the data, preprocessing, differential expression, isoform discovery, data visualization, and interpretation.
 </li>
 <li>
  <a href="http://rnaseq.uoregon.edu/">
   RNA-seqlopedia
  </a>
  - RNA-seqlopedia provides an awesome overview of RNA-seq and of the choices necessary to carry out a successful RNA-seq experiment.
 </li>
 <li>
  <a href="http://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0881-8">
   A survey of best practices for RNA-seq data analysis
  </a>
  - Gives awesome roadmap for RNA-seq computational analyses, including challenges/obstacles and things to look out for, but also how you might integrate RNA-seq data with other data types.
 </li>
 <li>
  <a href="https://www.youtube.com/watch?v=5NiFibnbE8o">
   Stories from the Supplement
  </a>
  [46:39] - Dr. Lior Pachter shares his stories from the supplement for well-known RNA-seq analysis software CuffDiff and
  <a href="http://cole-trapnell-lab.github.io/cufflinks/">
   Cufflinks
  </a>
  and explains some of their methodologies.
 </li>
 <li>
  <a href="https://en.wikipedia.org/wiki/List_of_RNA-Seq_bioinformatics_tools">
   List of RNA-seq Bioinformatics Tools
  </a>
  - Extensive list on Wikipedia of RNA-seq bioinformatics tools needed in analysis, ranging from all parts of an analysis pipeline from quality control, alignment, splice analysis, and visualizations.
 </li>
 <li>
  <a href="https://github.com/crazyhottommy/RNA-seq-analysis">
   RNA-seq Analysis
  </a>
  -
  <a href="https://github.com/crazyhottommy">
   @crazyhottommy
  </a>
  's notes on various steps and considerations when doing RNA-seq analysis.
 </li>
</ul>
<h3>
 ChIP-Seq
</h3>
<ul>
 <li>
  <a href="https://github.com/crazyhottommy/ChIP-seq-analysis">
   ChIP-seq analysis notes from Tommy Tang
  </a>
  - Resources on ChIP-seq data which include papers, methods, links to software, and analysis.
 </li>
</ul>
<h3>
 YouTube Channels and Playlists
</h3>
<ul>
 <li>
  <a href="https://www.genome.gov/12514288/current-topics-in-genome-analysis-2016-course-syllabus-handouts-and-videos/">
   Current Topics in Genome Analysis 2016
  </a>
  - Excellent series of fourteen lectures given at NIH about current topics in genomics ranging from sequence analysis, to sequencing technologies, and even more translational topics such as genomic medicine.
 </li>
 <li>
  <a href="https://www.youtube.com/user/GenomeTV">
   GenomeTV
  </a>
  - "GenomeTV is NHGRI's collection of official video resources from lectures, to news documentaries, to full video collections of meetings that tackle the research, issues and clinical applications of genomic research."
 </li>
 <li>
  <a href="https://www.youtube.com/user/LeadingStrand">
   Leading Strand
  </a>
  - Keynote lectures from Cold Spring Harbor Laboratory (CSHL) Meetings. More on
  <a href="http://theleadingstrand.cshl.edu/">
   The Leading Strand
  </a>
  .
 </li>
 <li>
  <a href="https://www.youtube.com/playlist?list=PLqLDR0CTP9_pboZCk6gR9Zn4kW7h9XWJI">
   Genomics, Big Data and Medicine Seminar Series
  </a>
  - "Our seminars are dedicated to the critical intersection of GBM, delving into 'bleeding edge' technology and approaches that will deeply shape the future."
 </li>
 <li>
  <a href="https://www.youtube.com/user/RafalabChannel/videos">
   Rafael Irizarry's Channel
  </a>
  - Dr. Rafael Irizarry's lectures and academic talks on statistics for genomics.
 </li>
 <li>
  <a href="https://www.youtube.com/user/nihvcast">
   NIH VideoCasting and Podcasting
  </a>
  - "NIH VideoCast broadcasts seminars, conferences and meetings live to a world-wide audience over the Internet as a real-time streaming video." Not exclusively genomics and bioinformatics video but many great talks on domain specific use of bioinformatics and genomics.
 </li>
</ul>
<h3>
 Blogs
</h3>
<ul>
 <li>
  <a href="http://www.acgt.me/">
   ACGT
  </a>
  - Dr. Keith Bradnam writes about this "thoughts on biology, genomics, and the ongoing threat to humanity from the bogus use of bioinformatics acroynums."
 </li>
 <li>
  <a href="http://www.opiniomics.org/">
   Opiniomics
  </a>
  - Dr. Mick Watson write on bioinformatics, genomes, and biology.
 </li>
 <li>
  <a href="https://liorpachter.wordpress.com/">
   Bits of DNA
  </a>
  - Dr. Lior Pachter writes review and commentary on computational biology.
 </li>
 <li>
  <a href="http://www.michaeleisen.org/blog/">
   it is NOT junk
  </a>
  - Dr. Michael Eisen writes "a blog about genomes, DNA, evolution, open science, baseball and other important things"
 </li>
</ul>
<h3>
 Miscellaneous
</h3>
<ul>
 <li>
  <a href="https://github.com/jtleek/genomicspapers/">
   The Leek group guide to genomics papers
  </a>
  - Expertly curated genomics papers to get up to speed on genomics, RNA-seq, statistics (used in genomics), software development, and more.
 </li>
 <li>
  <a href="http://dx.doi.org/10.1371/journal.pcbi.1003662">
   A New Online Computational Biology Curriculum
  </a>
  - "This article introduces a catalog of several hundred free video courses of potential interest to those wishing to expand their knowledge of bioinformatics and computational biology. The courses are organized into eleven subject areas modeled on university departments and are accompanied by commentary and career advice."
 </li>
 <li>
  <a href="http://www.foo.be/docs/tpj/issues/vol1_2/tpj0102-0001.html">
   How Perl Saved the Human Genome Project
  </a>
  - An anecdote by Lincoln D. Stein on the importance of the Perl programming language in the Human Genome Project.
 </li>
 <li>
  <a href="https://liacs.leidenuniv.nl/~hoogeboomhj/mcb/nature_primer.html">
   Educational Papers from Nature Biotechnology and PLoS Computational Biology
  </a>
  - Page of links to primers and short educational articles on various methods used in computational biology and bioinformatics.
 </li>
</ul>
<h2>
 License
</h2>
<p>
 <a href="https://creativecommons.org/publicdomain/zero/1.0/">
  <img alt="CC0" src="http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg"/>
 </a>
</p>
