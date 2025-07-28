

# Class: Homoeology (Homoeology) 


_Associations related to homoeology. Homoeologs are pairs of genes that originated by speciation _

_and were brought back together in the same genome by allopolyploidization (PMC4920642)._

__

_Allopolyploidization is the formation of new species through the combination of chromosomes from_

_different species._

__

_Based on the meaning of the term, this class is made a subclass of 'IntraSpeciesAssociation'._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:Homoeology](https://knetminer.com/terms/motifs/motif-categories/Homoeology)






```mermaid
 classDiagram
    class Homoeology
    click Homoeology href "../Homoeology"
      IntraSpeciesAssociation <|-- Homoeology
        click IntraSpeciesAssociation href "../IntraSpeciesAssociation"
      PhylogenyConfidentAssociation <|-- Homoeology
        click PhylogenyConfidentAssociation href "../PhylogenyConfidentAssociation"
      

      Homoeology <|-- HomoeologyAnn
        click HomoeologyAnn href "../HomoeologyAnn"
      Homoeology <|-- HomoeologyTraitAssn
        click HomoeologyTraitAssn href "../HomoeologyTraitAssn"
      Homoeology <|-- HomoeologyTextMining
        click HomoeologyTextMining href "../HomoeologyTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [PhylogenyConfidentAssociation](PhylogenyConfidentAssociation.md)
        * **Homoeology** [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
            * [HomoeologyAnn](HomoeologyAnn.md) [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]
            * [HomoeologyTraitAssn](HomoeologyTraitAssn.md) [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]
            * [HomoeologyTextMining](HomoeologyTextMining.md) [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:Homoeology |
| native | motif:Homoeology |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Homoeology
description: "Associations related to homoeology. Homoeologs are pairs of genes that\
  \ originated by speciation \nand were brought back together in the same genome by\
  \ allopolyploidization (PMC4920642).\n\nAllopolyploidization is the formation of\
  \ new species through the combination of chromosomes from\ndifferent species.\n\n\
  Based on the meaning of the term, this class is made a subclass of 'IntraSpeciesAssociation'.\n"
title: Homoeology
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhylogenyConfidentAssociation
abstract: true
mixins:
- IntraSpeciesAssociation

```
</details>

### Induced

<details>
```yaml
name: Homoeology
description: "Associations related to homoeology. Homoeologs are pairs of genes that\
  \ originated by speciation \nand were brought back together in the same genome by\
  \ allopolyploidization (PMC4920642).\n\nAllopolyploidization is the formation of\
  \ new species through the combination of chromosomes from\ndifferent species.\n\n\
  Based on the meaning of the term, this class is made a subclass of 'IntraSpeciesAssociation'.\n"
title: Homoeology
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhylogenyConfidentAssociation
abstract: true
mixins:
- IntraSpeciesAssociation

```
</details>