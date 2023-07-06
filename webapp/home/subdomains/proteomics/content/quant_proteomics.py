"""Content for data section - tools, workflows and help tabs."""

galaxy_au_support_item = {
    "title_html": 'Galaxy Australia support',
    "description_html": """<p>
            Any user of Galaxy Australia can request support through an
            online form.
        </p>""",
    "button_link": "/request/support",
    "button_html": "Request support",
}

tools = [
    # {   # Accordion item schema:
    #     "title_html": '',
    #     "description_html": """""",
    #     "inputs": [
    #         {
    #             'datatypes': [''],
    #             'label': '',
    #         },
    #     ],
    #     "button_link": "",
    #     "button_html": "",
    #     "button_tip": "",
    #     "view_link": "",
    #     "view_html": "",
    #     "view_tip": "",
    # },
    {
        "title_html": '<code>MaxQuant</code>',
        "description_html": '<p>MaxQuant is a quantitative proteomics software package designed for analyzing large mass-spectrometric data sets.</p>',
        "inputs": [
            {'datatypes': ['Thermo RAW']},
            {'datatypes': ['mzML']},
            {'datatypes': ['mzXML']},
            {'datatypes': ['Tabular file with experimental design template']}
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/2.0.3.0+galaxy0",
    },
    {
        "title_html": '<code>FlashLFQ</code>',
        "description_html": '<p>Ultrafast label-free quantification for mass-spectrometry proteomics.</p>',
        "inputs": [
            {'datatypes': ['Identification file'], label: 'MetaMorpheus, Morpheus, PeptideShaker PSM Report, MaxQuant'}
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=toolshed.g2.bx.psu.edu/repos/galaxyp/flashlfq/flashlfq/1.0.3.1",
    }
]