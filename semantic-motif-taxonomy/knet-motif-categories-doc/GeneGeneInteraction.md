

# Class: Gene-Gene Interaction (GeneGeneInteraction) 


_Associations related to interactions between genes, such as genetic interactions,_

_epistasis, or other forms of gene interactions, direct or indirect._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:GeneGeneInteraction](https://knetminer.com/terms/motifs/motif-categories/GeneGeneInteraction)






```mermaid
 classDiagram
    class GeneGeneInteraction
    click GeneGeneInteraction href "../GeneGeneInteraction"
      BioMolecularInteraction <|-- GeneGeneInteraction
        click BioMolecularInteraction href "../BioMolecularInteraction"
      

      GeneGeneInteraction <|-- GeneIntAnn
        click GeneIntAnn href "../GeneIntAnn"
      GeneGeneInteraction <|-- GeneIntTraitAnn
        click GeneIntTraitAnn href "../GeneIntTraitAnn"
      GeneGeneInteraction <|-- GeneIntTextMining
        click GeneIntTextMining href "../GeneIntTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BioMolecularInteraction](BioMolecularInteraction.md)
        * **GeneGeneInteraction**
            * [GeneIntAnn](GeneIntAnn.md) [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]
            * [GeneIntTraitAnn](GeneIntTraitAnn.md) [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]
            * [GeneIntTextMining](GeneIntTextMining.md) [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:GeneGeneInteraction |
| native | motif:GeneGeneInteraction |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneGeneInteraction
description: 'Associations related to interactions between genes, such as genetic
  interactions,

  epistasis, or other forms of gene interactions, direct or indirect.

  '
title: Gene-Gene Interaction
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: BioMolecularInteraction
abstract: true

```
</details>

### Induced

<details>
```yaml
name: GeneGeneInteraction
description: 'Associations related to interactions between genes, such as genetic
  interactions,

  epistasis, or other forms of gene interactions, direct or indirect.

  '
title: Gene-Gene Interaction
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: BioMolecularInteraction
abstract: true

```
</details>