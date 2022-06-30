import webbrowser


def open_in_pubmed(pubmed_id: str) -> bool:
    return webbrowser.open_new_tab('https://pubmed.ncbi.nlm.nih.gov/%s' % pubmed_id)


def open_in_dbsnp(variant_id: str) -> bool:
    return webbrowser.open_new_tab('https://www.ncbi.nlm.nih.gov/snp/%s' % variant_id)


def open_in_gtex(variant_id: str) -> bool:
    return webbrowser.open_new_tab('https://gtexportal.org/home/snp/%s' % variant_id)


def open_study_in_gwas_catalog(study_id: str) -> bool:
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/studies/%s' % study_id)


def open_variant_in_gwas_catalog(variant_id: str) -> bool:
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/variants/%s' % variant_id)


def open_trait_in_gwas_catalog(efo_id: str) -> bool:
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/efotraits/%s' % efo_id)


def open_gene_in_gwas_catalog(gene_name: str) -> bool:
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/genes/%s' % gene_name)


def open_region_in_gwas_catalog(region_name_or_location: str) -> bool:
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/regions/%s' % region_name_or_location)


def open_publication_in_gwas_catalog(pubmed_id: str) -> bool:
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/publications/%s' % pubmed_id)
