

## CLASSES

class NamedThing(object):
    """
    a databased entity or concept/class
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ThingWithTaxon(object):
    """
    A mixin that can be used on any entity with a taxon
    """
    def __init__(self,
                 in_taxon=None):
        self.in_taxon=in_taxon

    def __str__(self):
        return "in_taxon={} ".format(self.in_taxon)
    def __repr__(self):
        return self.__str__()


class OrganismTaxon(OntologyClass):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class IndividualOrganism(NamedThing):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class PopulationOfIndividualOrganisms(NamedThing):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Cohort(PopulationOfIndividualOrganisms):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Biosample(NamedThing):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ConditionOrPhenotypicFeature(OntologyClass):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Disease(ConditionOrPhenotypicFeature):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class PhenotypicFeature(ConditionOrPhenotypicFeature):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EnvironmentalFeature(NamedThing):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Provider(object):
    """
    person, group, organization or project that provides a piece of information
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class MolecularEntity(NamedThing):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalSubstance(MolecularEntity):
    """
    may be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class AnatomicalEntity(NamedThing):
    """
    A subcellular location, cell type or gross anatomical part
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class LifeStage(NamedThing):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class HasGenomicName(object):
    """
    None
    """
    def __init__(self,
                 full_name=None,
                 systematic_synonym=None):
        self.full_name=full_name
        self.systematic_synonym=systematic_synonym

    def __str__(self):
        return "full_name={} systematic_synonym={} ".format(self.full_name,self.systematic_synonym)
    def __repr__(self):
        return self.__str__()


class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneOrGeneProduct(GenomicEntity):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Gene(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneProduct(GeneOrGeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Protein(GeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class RnaProduct(GeneProduct):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class MacromolecularComplex(MolecularEntity):
    """
    None
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneGrouping(object):
    """
    any grouping of multiple genes or gene products
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Zygosity(object):
    """
    None
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
    """
    def __init__(self,
                 has_zygosity=None,
                 id=None,
                 label=None):
        self.has_zygosity=has_zygosity
        self.id=id
        self.label=label

    def __str__(self):
        return "has_zygosity={} id={} label={} ".format(self.has_zygosity,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class SequenceVariant(GenomicEntity):
    """
    A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus.
    """
    def __init__(self,
                 id=None,
                 label=None):
        self.id=id
        self.label=label

    def __str__(self):
        return "id={} label={} ".format(self.id,self.label)
    def __repr__(self):
        return self.__str__()


class Association(InformationContentEntity):
    """
    A typed association between two entities, supported by evidence
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class PairwiseGeneOrProteinInteractionAssociation(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity or substance and a gene or gene product. The chemical substance may be a drug with the gene being a target of the drug.
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
  
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EntityToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 frequency_qualifier=None,
                 severity_qualifier=None,
                 onset_qualifier=None,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.frequency_qualifier=frequency_qualifier
        self.severity_qualifier=severity_qualifier
        self.onset_qualifier=onset_qualifier
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "frequency_qualifier={} severity_qualifier={} onset_qualifier={} association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.frequency_qualifier,self.severity_qualifier,self.onset_qualifier,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class DiseaseToThingAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToThingAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToThingAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?
    """
    def __init__(self,
                 stage_qualifier=None,
                 quantifier_qualifier=None,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.stage_qualifier=stage_qualifier
        self.quantifier_qualifier=quantifier_qualifier
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "stage_qualifier={} quantifier_qualifier={} association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.stage_qualifier,self.quantifier_qualifier,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GoAssociation(Association):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class DenormalizedAssociation(Association):
    """
    An association that includes flattened inlined objects, such as subject_taxon_closure
    """
    def __init__(self,
                 subject_taxon=None,
                 subject_taxon_label=None,
                 subject_taxon_closure=None,
                 subject_taxon_closure_label=None,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.subject_taxon=subject_taxon
        self.subject_taxon_label=subject_taxon_label
        self.subject_taxon_closure=subject_taxon_closure
        self.subject_taxon_closure_label=subject_taxon_closure_label
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "subject_taxon={} subject_taxon_label={} subject_taxon_closure={} subject_taxon_closure_label={} association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.subject_taxon,self.subject_taxon_label,self.subject_taxon_closure,self.subject_taxon_closure_label,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class DiseaseToPhenotypicFeatureDenormalizedAssociation(DiseaseToPhenotypicFeatureAssociation):
    """
    None
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class AssociationResultSet(object):
    """
    None
    """
    def __init__(self,
                 associations=None):
        self.associations=associations

    def __str__(self):
        return "associations={} ".format(self.associations)
    def __repr__(self):
        return self.__str__()


class PropertyValuePair(object):
    """
    None
    """
    def __init__(self,
                 relation=None,
                 filler=None):
        self.relation=relation
        self.filler=filler

    def __str__(self):
        return "relation={} filler={} ".format(self.relation,self.filler)
    def __repr__(self):
        return self.__str__()


class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
    """
    def __init__(self,
                 start_interbase_coordinate=None,
                 end_interbase_coordinate=None,
                 genome_build=None,
                 phase=None,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.start_interbase_coordinate=start_interbase_coordinate
        self.end_interbase_coordinate=end_interbase_coordinate
        self.genome_build=genome_build
        self.phase=phase
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "start_interbase_coordinate={} end_interbase_coordinate={} genome_build={} phase={} association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.start_interbase_coordinate,self.end_interbase_coordinate,self.genome_build,self.phase,self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class SequenceFeatureToSequenceRelationship(Association):
    """
    Relates a sequence feature such as a gene to its sequence
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    def __init__(self,
                 association_type=None,
                 subject=None,
                 negated=None,
                 relation=None,
                 object=None,
                 qualifiers=None,
                 subject_extensions=None,
                 object_extensions=None,
                 publications=None,
                 provided_by=None,
                 has_evidence_graph=None,
                 has_evidence_type=None,
                 has_evidence=None,
                 id=None,
                 label=None):
        self.association_type=association_type
        self.subject=subject
        self.negated=negated
        self.relation=relation
        self.object=object
        self.qualifiers=qualifiers
        self.subject_extensions=subject_extensions
        self.object_extensions=object_extensions
        self.publications=publications
        self.provided_by=provided_by
        self.has_evidence_graph=has_evidence_graph
        self.has_evidence_type=has_evidence_type
        self.has_evidence=has_evidence
        self.id=id
        self.label=label

    def __str__(self):
        return "association_type={} subject={} negated={} relation={} object={} qualifiers={} subject_extensions={} object_extensions={} publications={} provided_by={} has_evidence_graph={} has_evidence_type={} has_evidence={} id={} label={} ".format(self.association_type,self.subject,self.negated,self.relation,self.object,self.qualifiers,self.subject_extensions,self.object_extensions,self.publications,self.provided_by,self.has_evidence_graph,self.has_evidence_type,self.has_evidence,self.id,self.label)
    def __repr__(self):
        return self.__str__()


class MolecularEvent(object):
    """
    None
    """
    def __init__(self):
        pass

    def __str__(self):
        return "".format()
    def __repr__(self):
        return self.__str__()


class BioentityWithGoTerms(MolecularEntity):
    """
    this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information
    """
    def __init__(self,
                 isa_partof_closure=None,
                 regulates_closure=None,
                 id=None,
                 label=None):
        self.isa_partof_closure=isa_partof_closure
        self.regulates_closure=regulates_closure
        self.id=id
        self.label=label

    def __str__(self):
        return "isa_partof_closure={} regulates_closure={} id={} label={} ".format(self.isa_partof_closure,self.regulates_closure,self.id,self.label)
    def __repr__(self):
        return self.__str__()


