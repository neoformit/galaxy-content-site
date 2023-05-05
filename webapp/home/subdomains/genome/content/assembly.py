"""Content for assembly section."""

from .data import galaxy_au_support_item

import_workflow_tip = "Import to Galaxy Australia"
view_workflow_tip = "View in WorkflowHub"

tools = [
    {
        "title_html": '<code>Hifiasm</code> - assembly with PacBio HiFi data',
        "description_html": """
            <p>
              A haplotype-resolved assembler for PacBio HiFi reads.
            </p>""",
        "inputs": [
            {'datatypes': ['fasta']},
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fbgruening%2Fhifiasm%2Fhifiasm",
    },
    {
        "title_html": '<code>Flye</code> - assembly with PacBio or Nanopore data',
        "description_html": """
            <p>
              <em>de novo</em> assembly of single-molecule sequencing reads,
              designed for a wide range of datasets, from small bacterial
              projects to large mammalian-scale assemblies.
              </p>""",
        "inputs": [
            {'datatypes': ['fasta']},
            {'datatypes': ['fastq']},
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fbgruening%2Fflye%2Fflye",
    },
    {
        "title_html": '<code>Unicycler</code> - assembly with Illumina, PacBio or Nanopore data - bacteria only',
        "description_html": """
            <p>
              Hybrid assembly pipeline for bacterial genomes, uses both Illumina reads and long reads (PacBio or Nanopore).
              </p>""",
        "inputs": [
            {'datatypes': ['fastq']},
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Funicycler%2Funicycler",
    },   
    {
        "title_html": '<code>Salsa</code> - scaffold assembly with HiC data',
        "description_html": """
            <p>
              Salsa is a scaffolding tool based on a computational method that
              exploits the genomic proximity information in Hi-C data sets
              for long-range scaffolding of <em>de novo</em> genome assemblies.
            </p>""",
        "inputs": [
            {'datatypes': ['fasta']},
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fsalsa%2Fsalsa",
    },
    {
        "title_html": '<code>Quast</code> - assess genome assembly quality',
        "description_html": """
            <p>
              QUAST = QUality ASsessment Tool. The tool evaluates genome assemblies by computing various metrics. If you have one or multiple genome assemblies, you can assess their quality with Quast. It works with or without reference genome
            </p>""",
        "inputs": [
            {'datatypes': ['fasta']},
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fquast%2Fquast",
    },
    {
        "title_html": '<code>Busco</code> - assess genome assembly quality',
        "description_html": """
            <p>
              BUSCO: assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs. The tool attempts to provide a quantitative assessment of the completeness in terms of the expected gene content of a genome assembly, transcriptome, or annotated gene set.
            </p>""",
        "inputs": [
            {'datatypes': ['fasta']},
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fbusco%2Fbusco",
    },
]


workflows_pacbio = [
    {
        "title_html": 'About these workflows',
        "description_html": """
            <p>
              This
              <a
                href="https://australianbiocommons.github.io/how-to-guides/genome_assembly/hifi_assembly"
                target="_blank"
              >
                How-to-Guide
              </a>
              will describe the steps required to assemble your genome on the Galaxy Australia platform, using multiple workflows.
            </p>""",
    },
    {
        "title_html": 'BAM to FASTQ + QC v1.0',
        "description_html": """
            <p>
              Convert a BAM file to FASTQ format to perform QC analysis
              (required if your data is in BAM format).
            </p>""",
        "inputs": [
            {
                'datatypes': ['bam'],
                'label': 'PacBio <em>subreads.bam</em>',
            },
        ],
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=220",
        "button_tip": import_workflow_tip,
        "view_link": "https://workflowhub.eu/workflows/220",
        "view_tip": view_workflow_tip,
    },
    {
        "title_html": 'PacBio HiFi genome assembly using hifiasm v2.1',
        "description_html": """
            <p>
              Assemble a genome using PacBio HiFi reads.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fastqsanger'],
                'label': 'HiFi reads',
            },
        ],
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=221",
        "button_tip": import_workflow_tip,
        "view_link": "https://workflowhub.eu/workflows/221",
        "view_tip": view_workflow_tip,
    },
    {
        "title_html": 'Purge duplicates from hifiasm assembly v1.0',
        "description_html": """
            <p>
              Optional workflow to purge duplicates from the contig assembly.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fastqsanger'],
                'label': 'HiFi reads',
            },
            {
                'datatypes': ['fasta'],
                'label': 'Primary assembly contigs',
            },
        ],
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=237",
        "button_tip": import_workflow_tip,
        "view_link": "https://workflowhub.eu/workflows/237",
        "view_tip": view_workflow_tip,
    },
    {
        "title_html": 'Genome assessment post-assembly',
        "description_html": """
            <p>
              Evaluate the quality of your genome assembly with a comprehensive report including <code>FASTA stats</code>, <code>BUSCO</code>, <code>QUAST</code>, <code>Meryl</code> and <code>Merqury</code>.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Primary assembly contigs',
            },
        ],
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=403",
        "button_tip": import_workflow_tip,
        "view_link": "https://workflowhub.eu/workflows/403",
        "view_tip": view_workflow_tip,
    },
]

workflows_nanopore = [
    {
        "title_html": 'About these workflows',
        "description_html": """
            <p>
              This
              <a
                href="https://training.galaxyproject.org/training-material/topics/assembly/tutorials/largegenome/tutorial.html"
                target="_blank"
              >
                tutorial
              </a>
              describes the steps required to assemble a genome on Galaxy with Nanopore and Illumina data.
            </p>""",
    },
    {
        "title_html": 'Flye assembly with Nanopore data',
        "description_html": """
            <p>
              Assemble Nanopore long reads. This workflow can be run alone or as part of a combined workflow for large genome assembly.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fastqsanger'],
                'label': 'Long reads (may be raw, filtered and/or corrected)',
            },
        ],
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=225",
        "button_tip": import_workflow_tip,
        "view_link": "https://workflowhub.eu/workflows/225",
        "view_tip": view_workflow_tip,
    },
    {
        "title_html": 'Assembly polishing',
        "description_html": """
            <p>
              Polishes (corrects) an assembly, using long reads (<code>Racon</code> and <code>Medaka</code>) and short reads (<code>Racon</code>).
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Assembly to polish',
            },
            {
                'datatypes': ['fastq'],
                'label': 'Long reads (those used in assembly)',
            },
            {
                'datatypes': ['fastq'],
                'label': 'Short reads to be used for polishing (R1 only)',
            },
        ],
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=226",
        "button_tip": import_workflow_tip,
        "view_link": "https://workflowhub.eu/workflows/226",
        "view_tip": view_workflow_tip,
    },
    {
        "title_html": 'Assess genome quality',
        "description_html": """
            <p>
              Assesses the quality of the genome assembly. Generates statistics, determines if expected genes are present and align contigs to a reference genome.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Polished assembly',
            },
            {
                'datatypes': ['fasta'],
                'label': 'Reference genome assembly (e.g. related species)',
            },
        ],
        "view_link": "https://workflowhub.eu/workflows/229",
        "view_tip": view_workflow_tip,
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=229",
        "button_tip": import_workflow_tip,
    },
]

workflows_hic = [
    {
        "title_html": 'About these workflows',
        "description_html": """
            <p>
              These workflows have been developed as part of the global Vertebrate Genome Project (VGP). A complete guide can be found
              <a
                href="https://galaxyproject.org/projects/vgp/workflows/"
                target="_blank"
              >here</a>.
              There are many different ways that these workflows can be used in practice - for a comprehensive example, check out this
              <a
                href="https://training.galaxyproject.org/training-material/topics/assembly/tutorials/vgp_genome_assembly/tutorial.html"
                target="_blank">Galaxy tutorial</a>.
            </p>""",
    },
    {
        "title_html": 'Kmer profiling',
        "description_html": """
            <p>
              This workflow produces a Meryl database and Genomescope outputs that will be used to determine parameters for following workflows, and assess the quality of genome assemblies. Specifically, it provides information about the genomic complexity, such as the genome size and levels of heterozygosity and repeat content, as well about the data quality.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fastq'],
                'label': 'PacBio HiFi reads',
            },
        ],
        "view_link": "https://dockstore.org/workflows/github.com/Delphine-L/iwc/WF1-kmer_profiling_and_QC:VGP",
        "view_tip": view_workflow_tip,
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=dockstore.org&trs_id=%23workflow/github.com/Delphine-L/iwc/WF1-kmer_profiling_and_QC",
        "button_tip": import_workflow_tip,
    },
    {
        "title_html": 'Hifi assembly and HiC phasing',
        "description_html": """
            <p>
              This workflow uses <code>hifiasm</code> (HiC mode) to generate HiC-phased haplotypes (<code>hap1</code> and <code>hap2</code>). This is in contrast to its default mode, which generates primary and alternate pseudohaplotype assemblies. This workflow includes three tools for evaluating assembly quality: <code>gfastats</code>, <code>BUSCO</code> and <code>Merqury</code>.
            </p>

            <p>
              <small>
                Note: if you have multiple input files for each HiC set, they need to be concatenated. The forward set needs to be concatenated in the same order as reverse set.
              </small>
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'PacBio HiFi reads',
            },
            {
                'datatypes': ['fastq'],
                'label': 'PacBio HiC reads (forward)',
            },
            {
                'datatypes': ['fastq'],
                'label': 'PacBio HiC reads (reverse)',
            },
            {
                'datatypes': ['meryldb'],
                'label': '<code<Meryl</code> kmer database',
            },
            {
                'datatypes': ['txt'],
                'label': '<code>GenomeScope</code> genome profile summary',
            },
        ],
        "view_link": "https://dockstore.org/workflows/github.com/Delphine-L/iwc/WF4-Assembly_with_HiC:VGP",
        "view_tip": view_workflow_tip,
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=dockstore.org&trs_id=%23workflow/github.com/Delphine-L/iwc/WF4-Assembly_with_HiC",
        "button_tip": import_workflow_tip,
    },
    {
        "title_html": 'Purge duplicates',
        "description_html": """
            <p>
              This workflow identifies and reassigns heterozygous contigs.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': '<code>hifiasm</code> primary assembly - <code>hap1</code>',
            },
            {
                'datatypes': ['fasta'],
                'label': '<code>hifiasm</code> alternate assembly - <code>hap2</code>',
            },
            {
                'datatypes': ['fasta', 'fastq'],
                'label': 'Trimmed PacBio reads',
            },
            {
                'datatypes': ['meryldb'],
                'label': '<code<Meryl</code> kmer database',
            },
            {
                'datatypes': ['txt'],
                'label': '<code>GenomeScope</code> model parameters',
            },
        ],
        "view_link": "https://dockstore.org/workflows/github.com/Delphine-L/iwc/WF6-Purgedups:VGP",
        "view_tip": view_workflow_tip,
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=dockstore.org&trs_id=%23workflow/github.com/Delphine-L/iwc/WF6-Purgedups",
        "button_tip": import_workflow_tip,
    },
    {
        "title_html": 'HiC scaffolding',
        "description_html": """
            <p>
              This workflow scaffolds the assembly contigs using information from HiC data.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Assembly',
            },
            {
                'datatypes': ['fastq'],
                'label': 'HiC forward reads',
            },
            {
                'datatypes': ['fastq'],
                'label': 'HiC reverse reads',
            },
        ],
        "view_link": "https://dockstore.org/workflows/github.com/Delphine-L/iwc/WF8a-Scaffolding_HiC_Yahs:VGP",
        "view_tip": view_workflow_tip,
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=dockstore.org&trs_id=%23workflow/github.com/Delphine-L/iwc/WF8a-Scaffolding_HiC_Yahs",
        "button_tip": import_workflow_tip,
    },
    {
        "title_html": 'Decontamination',
        "description_html": """
            <p>
              This workflow identifies and removes contaminants from the assembly.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Assembly',
            },
        ],
        "view_link": "https://dockstore.org/workflows/github.com/Delphine-L/iwc/WF9-Decontamination:VGP",
        "view_tip": view_workflow_tip,
        "button_link": "https://usegalaxy.org.au/workflows/trs_import?trs_server=dockstore.org&trs_id=%23workflow/github.com/Delphine-L/iwc/WF9-Decontamination",
        "button_tip": import_workflow_tip,
    },
]

workflows = {
    'subsections': [
        {
            'id': 'pacbio',
            'title': 'Assembly with PacBio HiFi data',
            'content': workflows_pacbio,
        },
        {
            'id': 'nanopore',
            'title': 'Assembly with Nanopore data and polishing with Illumina data',
            'content': workflows_nanopore,
        },
        {
            'id': 'hic',
            'title': 'Assembly with PacBio HiFi and HiC data',
            'content': workflows_hic,
        },
    ]
}


help = [
    {
        "title_html": 'Can I use Galaxy Australia to assemble a large genome?',
        "description_html": """
            <p>
              Yes. Galaxy Australia has assembly tools for small prokaryote genomes as well as larger eukaryote genomes. We are continually adding new tools and optimising them for large genome assemblies - this means adding enough computer processing power to run data-intensive tools, as well as configuring aspects such as parallelisation.
            </p>
            <p>
              Please contact us if:
            </p>
            <ul>
              <li>you need to increase your data storage limit</li>
              <li>there is a tool you wish to request</li>
              <li>a tool appears to be broken or running slowly</li>
            </ul>""",
        "button_link": "/request",
        "button_html": "Request support",
    },
    {
        "title_html": 'How can I learn about genome assembly?',
        "description_html": """
            <ul>
              <li>See the tutorials in this Help section. They cover different approaches to genome assembly.
              </li>
              <li>Read the methods in scientific papers about genome assembly, particularly those about genomes with similar characteristics to those in your project</li>
              <li>See the Workflows section for examples of different approaches to genome assembly - these cover different sequencing data types, and a variety of tools.</li>
            </ul>""",
    },
    {
        "title_html": 'Genome assembly overview',
        "description_html": """
            <p>Genome assembly can be a very involved process. A typical genome assembly procedure might look like:</p>
            <ul>
              <li>Data QC - check the quality and characteristics of your sequencing reads.</li>
              <li>Kmer counting - to determine genome characteristics such as ploidy and size.</li>
              <li>Data preparation - trimming and filtering sequencing reads if required.</li>
              <li>Assembly - for large genomes, this is usually done with long sequencing reads from PacBio or Nanopore.</li>
              <li>Polishing - the assembly may be polished (corrected) with long and/or short (Illumina) reads.</li>
              <li>Scaffolding - the assembly contigs may be joined together with other sequencing data such as HiC.</li>
              <li>Assessment - at any stage, the assembly can be assessed for number of contigs, number of base pairs, whether expected genes are present, and many other metrics.</li>
              <li>Annotation - identify features on the genome assembly such as gene names and locations.</li>
            </ul>
            <img class="img-fluid" src="/static/home/img/subdomains/genome/assembly-overview.png" alt="Genome assembly flowchart">
            <p class="text-center">A graphical representation of genome assembly</p>""",
    },
    {
        "title_html": 'Which tools should I use?',
        "description_html": """
            <p>
              There is no best set of tools to recommend - new tools are developed constantly, sequencing technology improves rapidly, and many genomes have never been sequenced before and thus their characteristics and quirks are unknown. The "Tools" tab in this section includes a list of commonly-used tools that could be a good starting point. You will find other tools in recent publications or used in workflows.
            </p>
            <p>
              You can also search for tools in Galaxy's tool panel. If they aren't installed on Galaxy Australia, you can
              <a href="/request/tool">request installation</a>
              of a tool.
            </p>
            <p>
              We recommend testing a tool on a small data set first and seeing if the results make sense, before running on your full data set.
            </p>
        """,
    },
    {
        "title_html": 'Tutorials',
        "description_html": """
            <p>
                Find 15+ Galaxy training tutorials
                <a
                href="https://training.galaxyproject.org/training-material/topics/assembly/"
                target="_blank"
                >here</a>.
            </p>

            <p>
                <a
                href="https://training.galaxyproject.org/training-material/topics/assembly/tutorials/get-started-genome-assembly/slides.html#1"
                target="_blank"
                >
                Introduction to genome assembly and annotation (slides)
                </a>
            </p>

            <p>
                <a
                href="https://training.galaxyproject.org/training-material/topics/assembly/tutorials/vgp_genome_assembly/tutorial.html"
                target="_blank"
                >
                Vertebrate genome assembly pipeline (tutorial)
                </a>
            </p>

            <p>
                <a
                href="https://training.galaxyproject.org/training-material/topics/assembly/tutorials/largegenome/tutorial.html"
                target="_blank"
                >
                Nanopore and illumina genome assembly (tutorial)
                </a>
            </p>

            <p>
                <a
                href="https://gxy.io/GTN:T00165"
                target="_blank"
                >
                Share workflows and results with workflow reports (tutorial)
                </a>
            </p>
        """,
    },
    {
        "title_html": 'How can I assess the quality of my genome assembly?',
        "description_html": """
            <p>
              Once a genome has been assembled, it is important to assess the quality of the assembly, and in the first instance, this quality control (QC) can be achieved using the workflow described here.
            </p>
        """,
        "button_link": "https://australianbiocommons.github.io/how-to-guides/genome_assembly/assembly_qc",
        "button_html": "Workflow tutorial",
    },
    galaxy_au_support_item,
]
