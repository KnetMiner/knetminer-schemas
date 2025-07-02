

# Class: Intra-Specie Association (IntraSpecieAssociation) 


_Associations in this category are based on the same specie of the gene that is considered, contrary_

_to, eg, homology or sequence similarity._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:IntraSpecieAssociation](https://knetminer.com/terms/motifs/motif-categories/IntraSpecieAssociation)






```mermaid
 classDiagram
    class IntraSpecieAssociation
    click IntraSpecieAssociation href "../IntraSpecieAssociation"
      AssociationStrength <|-- IntraSpecieAssociation
        click AssociationStrength href "../AssociationStrength"
      

      IntraSpecieAssociation <|-- IntraTraitAssn
        click IntraTraitAssn href "../IntraTraitAssn"
      IntraSpecieAssociation <|-- GeneExpression
        click GeneExpression href "../GeneExpression"
      IntraSpecieAssociation <|-- Homoeology
        click Homoeology href "../Homoeology"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [AssociationStrength](AssociationStrength.md)
        * **IntraSpecieAssociation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [IntraTraitAssn](IntraTraitAssn.md) | A gene-trait association that is established with information and methods wit... |
| [GeneExpression](GeneExpression.md) | Associations of this type are related to gene expression, for instance becaus... |
| [Homoeology](Homoeology.md) | Associations related to homoeology |








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| associationStrength | 1 |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:IntraSpecieAssociation |
| native | motif:IntraSpecieAssociation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntraSpecieAssociation
annotations:
  associationStrength:
    tag: associationStrength
    value: 1
description: 'Associations in this category are based on the same specie of the gene
  that is considered, contrary

  to, eg, homology or sequence similarity.

  '
title: Intra-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AssociationStrength
abstract: true
mixin: true

```
</details>

### Induced

<details>
```yaml
name: IntraSpecieAssociation
annotations:
  associationStrength:
    tag: associationStrength
    value: 1
description: 'Associations in this category are based on the same specie of the gene
  that is considered, contrary

  to, eg, homology or sequence similarity.

  '
title: Intra-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AssociationStrength
abstract: true
mixin: true

```
</details>