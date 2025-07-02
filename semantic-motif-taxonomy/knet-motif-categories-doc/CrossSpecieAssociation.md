

# Class: Intra-Specie Association (CrossSpecieAssociation) 


_Associations in this category are obtained by comparing information in multiple species, eg,_

_via homology or sequence similarity.    _

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:CrossSpecieAssociation](https://knetminer.com/terms/motifs/motif-categories/CrossSpecieAssociation)






```mermaid
 classDiagram
    class CrossSpecieAssociation
    click CrossSpecieAssociation href "../CrossSpecieAssociation"
      AssociationStrength <|-- CrossSpecieAssociation
        click AssociationStrength href "../AssociationStrength"
      

      CrossSpecieAssociation <|-- Homology
        click Homology href "../Homology"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [AssociationStrength](AssociationStrength.md)
        * **CrossSpecieAssociation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Homology](Homology.md) | Associations related to homology, that it, cross-specie gene similarity resul... |








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| associationStrength | 2 |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:CrossSpecieAssociation |
| native | motif:CrossSpecieAssociation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrossSpecieAssociation
annotations:
  associationStrength:
    tag: associationStrength
    value: 2
description: "Associations in this category are obtained by comparing information\
  \ in multiple species, eg,\nvia homology or sequence similarity.    \n"
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
name: CrossSpecieAssociation
annotations:
  associationStrength:
    tag: associationStrength
    value: 2
description: "Associations in this category are obtained by comparing information\
  \ in multiple species, eg,\nvia homology or sequence similarity.    \n"
title: Intra-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AssociationStrength
abstract: true
mixin: true

```
</details>