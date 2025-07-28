

# Class: Intra-Specie Association (IntraSpeciesAssociation) 


_Associations in this category are based on the same species of the gene that is considered, contrary_

_to, eg, homology or sequence similarity._

__





URI: [motif:IntraSpeciesAssociation](https://knetminer.com/terms/motifs/motif-categories/IntraSpeciesAssociation)






```mermaid
 classDiagram
    class IntraSpeciesAssociation
    click IntraSpeciesAssociation href "../IntraSpeciesAssociation"
      SpeciesSpanQualifier <|-- IntraSpeciesAssociation
        click SpeciesSpanQualifier href "../SpeciesSpanQualifier"
      

      IntraSpeciesAssociation <|-- IntraSpeciesAnnotation
        click IntraSpeciesAnnotation href "../IntraSpeciesAnnotation"
      IntraSpeciesAssociation <|-- GeneExpression
        click GeneExpression href "../GeneExpression"
      IntraSpeciesAssociation <|-- Homoeology
        click Homoeology href "../Homoeology"
      
      
      
```





## Inheritance
* [SemanticMotifQualifier](SemanticMotifQualifier.md)
    * [SpeciesSpanQualifier](SpeciesSpanQualifier.md)
        * **IntraSpeciesAssociation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [IntraSpeciesAnnotation](IntraSpeciesAnnotation.md) | Annotations between genes and other entities that are within the same species |
| [GeneExpression](GeneExpression.md) | Associations of this type are related to gene expression, for instance becaus... |
| [Homoeology](Homoeology.md) | Associations related to homoeology |








## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:IntraSpeciesAssociation |
| native | motif:IntraSpeciesAssociation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntraSpeciesAssociation
description: 'Associations in this category are based on the same species of the gene
  that is considered, contrary

  to, eg, homology or sequence similarity.

  '
title: Intra-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SpeciesSpanQualifier
mixin: true

```
</details>

### Induced

<details>
```yaml
name: IntraSpeciesAssociation
description: 'Associations in this category are based on the same species of the gene
  that is considered, contrary

  to, eg, homology or sequence similarity.

  '
title: Intra-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SpeciesSpanQualifier
mixin: true

```
</details>