

# Class: Cross-Specie Association (CrossSpeciesAssociation) 


_Associations in this category are obtained by comparing information across species, eg,_

_via homology or sequence similarity._

__





URI: [motif:CrossSpeciesAssociation](https://knetminer.com/terms/motifs/motif-categories/CrossSpeciesAssociation)






```mermaid
 classDiagram
    class CrossSpeciesAssociation
    click CrossSpeciesAssociation href "../CrossSpeciesAssociation"
      SpeciesSpanQualifier <|-- CrossSpeciesAssociation
        click SpeciesSpanQualifier href "../SpeciesSpanQualifier"
      

      CrossSpeciesAssociation <|-- Homology
        click Homology href "../Homology"
      
      
      
```





## Inheritance
* [SemanticMotifQualifier](SemanticMotifQualifier.md)
    * [SpeciesSpanQualifier](SpeciesSpanQualifier.md)
        * **CrossSpeciesAssociation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Homology](Homology.md) | Associations related to homology, that it, cross-species gene similarity resu... |








## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:CrossSpeciesAssociation |
| native | motif:CrossSpeciesAssociation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrossSpeciesAssociation
description: 'Associations in this category are obtained by comparing information
  across species, eg,

  via homology or sequence similarity.

  '
title: Cross-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SpeciesSpanQualifier
mixin: true

```
</details>

### Induced

<details>
```yaml
name: CrossSpeciesAssociation
description: 'Associations in this category are obtained by comparing information
  across species, eg,

  via homology or sequence similarity.

  '
title: Cross-Specie Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SpeciesSpanQualifier
mixin: true

```
</details>