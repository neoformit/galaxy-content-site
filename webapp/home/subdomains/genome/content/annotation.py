"""Content for annotation section."""

from .data import galaxy_au_support_item

tools = [
    {
        "title_html": '<code>MAKER</code> - genome annotation pipeline',
        "description_html": """
            <p>
                MAKER is able to annotate both prokaryotes and eukaryotes. It works by aligning as many evidences as possible along the genome sequence, and then reconciliating all these signals to determine probable gene structures.
                <br><br>
                The evidences can be transcript or protein sequences from the same (or closely related) organism. These sequences can come from public databases (like NR or GenBank) or from your own experimental data (transcriptome assembly from an RNASeq experiment for example). MAKER is also able to take into account repeated elements.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assembly',
            },
            {
                'datatypes': ['fasta'],
                'label': 'Protein evidence (optional)',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fmaker%2Fmaker",
    },
    {
        "title_html": '<code>Funannotate predict</code> - predicted gene annotations',
        "description_html": """
            <p>
              <code>Funannotate predict</code> performs a comprehensive whole genome gene prediction. Uses AUGUSTUS, GeneMark, Snap, GlimmerHMM, BUSCO, EVidence Modeler, tbl2asn, tRNAScan-SE, Exonerate, minimap2. This approach differs from Maker as it does not need to train <em>ab initio</em> predictors
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assembly (soft-masked)',
            },
            {
                'datatypes': ['bam'],
                'label': 'Mapped RNA evidence (optional)',
            },
            {
                'datatypes': ['fasta'],
                'label': 'Protein evidence (optional)',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Ffunannotate_predict%2Ffunannotate_predict",
    },
    {
        "title_html": '<code>RepeatMasker</code> - screen DNA sequences for interspersed repeats and low complexity regions',
        "description_html": """
            <p>
                RepeatMasker is a program that screens DNA for repeated elements such as tandem repeats, transposons, SINEs and LINEs. Galaxy AU has installed the full and curated DFam screening databases, or a custom database can be provided in <code>fasta</code> format. Additional reference data can be downloaded from
                <a
                  href="https://www.girinst.org/repbase/"
                  target="_blank">
                  RepBase</a>.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assembly',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fbgruening%2Frepeat_masker%2Frepeatmasker_wrapper",
    },
    {
        "title_html": '<code>InterProScan</code> - Scans InterPro database and assigns functional annotations',
        "description_html": """
            <p>
                Interproscan is a batch tool to query the InterPro database. It provides annotations based on multiple searches of profile and other functional databases.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assembly',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fbgruening%2Finterproscan%2Finterproscan",
    },
    {
        "title_html": '<code>Funannotate compare</code> - compare several annotations',
        "description_html": """
            <p>
                <code>Funannotate compare</code> compares several annotations and outputs a GFF3 file with the best gene models. It can be used to compare the results of different gene predictors, or to compare the results of a gene predictor with a reference annotation.
            </p>""",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assemblies to compare',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Ffunannotate_compare%2Ffunannotate_compare",
    },
    {
        "title_html": '<code>JBrowse</code> - Genome browser to visualize annotations',
        "description_html": "",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assembly',
            },
            {
                'datatypes': ['gff', 'gff3', 'bed'],
                'label': 'Annotations',
            },
            {
                'datatypes': ['bam'],
                'label': 'Mapped RNAseq data (optional)',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fjbrowse%2Fjbrowse",
    },
    {
        "title_html": '<code>Prokka</code> - Genome annotation, prokaryotes only',
        "description_html": "",
        "inputs": [
            {
                'datatypes': ['fasta'],
                'label': 'Genome assembly',
            },
        ],
        "button_link": "https://usegalaxy.org.au/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fcrs4%2Fprokka%2Fprokka",
    },
]

workflows = [
    {
        "title_html": 'Annotation with Maker',
        "description_html": """
            <p>
              Annotates a genome using multiple rounds of Maker, including gene prediction using SNAP and Augustus.
              <br>
              <br>
              Tools:
              <code>maker</code>
              <code>snap</code>
              <code>augustus</code>
              <code>busco</code>
              <code>jbrowse</code>
            </p>""",
        "inputs": [
             {
                'datatypes': ['fasta'],
                'label': 'Genome assembly',
            },
            {
                'datatypes': ['fastq'],
                'label': 'RNAseq Illumina reads',
            },
            {
                'datatypes': ['fasta'],
                'label': 'Proteins',
            },
        ],
        "button_link": "https://usegalaxy.org.au/u/anna/w/genome-annotation-with-maker",
        "button_tip": "Run in Galaxy AU",
    },
    {
        "title_html": 'Annotation with Funannotate',
        "description_html": """
            <p>
              Annotates a genome using Funannotate, includes RNAseq data with RNAstar, and protein predictions from EggNOG.
              <br>
              <br>
              Tools:
              <code>RNAstar</code>
              <code>funannotate</code>
              <code>eggnog</code>
              <code>busco</code>
              <code>jbrowse</code>
               <code>aegean parseval</code>
            </p>""",
        "inputs": [
             {
                'datatypes': ['fasta'],
                'label': 'Genome assembly (soft-masked)',
            },
            {
                'datatypes': ['fastq'],
                'label': 'RNAseq Illumina reads',
            },
            {
                'datatypes': ['gff3'],
                'label': 'Alternative annotation',
            },
            {
                'datatypes': ['gbk'],
                'label': 'Alternative annotation',
            },
        ],
        "button_link": "https://usegalaxy.org.au/u/anna/w/annotation-funannotate",
        "button_tip": "Run in Galaxy AU",
    },
]

help = [
    {
        "title_html": 'What is genome annotation?',
        "description_html": """
            <p>
                These
                <a
                  href="https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/introduction/slides.html#1"
                  target="_blank"
                >
                  slides
                </a>
                from the Galaxy training network explain the process of genome annotation in detail. You can use the <code style="font-size: 1.5rem;">&larr;</code> and <code style="font-size: 1.5rem;">&rarr;</code> keys to navigate through the slides.
            </p>""",
    },
    {
        "title_html": 'Genome annotation overview',
        "description_html": """
            <p>The flowchart below shows how you might use your input data (in green) with different Galaxy tools (in blue) to annotate a genome assembly. For example, one pathway would be taking an assembled genome, plus information about repeats, and data from RNA-seq, to run in the Maker pipeline. The annotatations can then be viewed in JBrowse.</p>
            <img class="img-fluid" src="/static/home/img/subdomains/genome/annotation-overview.png" alt="Genome annotation flowchart">
            <p class="text-center">A graphical representation of genome annotation</p>""",
    },
    {
        "title_html": 'Can I use Fgenesh++ for annotation?',
        "description_html": """
            <p>
              <a
                href="http://www.softberry.com/berry.phtml?group=help&subgroup=pipelines&topic=fgenesh_plus_plus"
                target="_blank"
              >
                Fgenesh++
              </a>
              is a bioinformatics pipeline for automatic prediction of genes in eukaryotic genomes. It is presently not installed in Galaxy Australia, but the Australian Biocommons and partners have licensed the software and made it available via commandline. Australian researchers can apply for access through the Australian BioCommons.
            </p>
        """,
        'button_html': 'Apply',
        'button_link': 'https://www.biocommons.org.au/fgenesh-plus-plus',
        'button_tip': 'Apply for access to Fgenesh++',
    },
    {
        "title_html": 'Can I use Apollo to  share and edit the annotated genome?',
        "description_html": """
            <p>
                Apollo is web-browser accessible system that lets you conduct real-time collaborative curation and editing of genome annotations.
              </p>
              <p>
                The Australian BioCommons and our partners at QCIF and Pawsey provide a hosted
                <a href="https://apollo-portal.genome.edu.au/" target="_blank">
                  Apollo Portal service
                </a>
                where your genome assembly and supporting evidence files can be hosted. All system administration is taken care of, so you and your team can focus on the annotation curation itself.
            </p>

            <p>
                This
                <a href="https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/apollo-euk/tutorial.html" target="_blank">
                  Galaxy tutorial
                </a>
                provides a complete walkthrough of the process of refining eukaryotic genome annotations with Apollo.
            </p>
        """,
        "button_link": "https://support.biocommons.org.au/support/solutions/articles/6000244843-apollo-for-collaborative-curation-and-editing",
        "button_html": "More info",
    },
    {
        "title_html": 'Tutorials',
        "description_html": """
            <p class="lead">Genome annotation with Maker</p>
            <p>
                Genome annotation of eukaryotes is a little more complicated than for prokaryotes: eukaryotic genomes are usually larger than prokaryotes, with more genes. The sequences determining the beginning and the end of a gene are generally less conserved than the prokaryotic ones. Many genes also contain introns, and the limits of these introns (acceptor and donor sites) are not highly conserved. This
                <a
                  href="https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/annotation-with-maker/tutorial.html"
                  target="_blank"
                >
                  Galaxy tutorial
                </a>
                uses MAKER to annotate the genome of a small eukaryote: Schizosaccharomyces pombe (a yeast).
            </p>

            <hr>

            <p class="lead">Genome annotation with Funannotate</p>
            <p>
                This
                <a href="https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/funannotate/tutorial.html" target="_blank">
                  Galaxy tutorial
                </a>
                provides a complete walkthrough of the process of annotation with Funannotate, including the preparation of RNAseq data, structural annotation, functional annotation, visualisation, and comparing annotations.
            </p>
            """,
    },
    # {
    #     "title_html": '',
    #     "description_html": """""",
    #     "button_link": "",
    #     "button_html": "",
    # },
    galaxy_au_support_item,
]
