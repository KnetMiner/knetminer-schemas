

# Class: Text Mining Annotation (TextMiningAnnotation) 


_An association that was computed via text mining methods, such as name-entity recognition,_

_semantic similarity or LLM-based embeddings._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:TextMiningAnnotation](https://knetminer.com/terms/motifs/motif-categories/TextMiningAnnotation)






```mermaid
 classDiagram
    class TextMiningAnnotation
    click TextMiningAnnotation href "../TextMiningAnnotation"
      ComputationallyInferredAssociation <|-- TextMiningAnnotation
        click ComputationallyInferredAssociation href "../ComputationallyInferredAssociation"
      AnnotationMethod <|-- TextMiningAnnotation
        click AnnotationMethod href "../AnnotationMethod"
      

      TextMiningAnnotation <|-- RegulationTextMining
        click RegulationTextMining href "../RegulationTextMining"
      TextMiningAnnotation <|-- PhysInteractTextMining
        click PhysInteractTextMining href "../PhysInteractTextMining"
      TextMiningAnnotation <|-- GeneIntTextMining
        click GeneIntTextMining href "../GeneIntTextMining"
      TextMiningAnnotation <|-- HomoeologyTextMining
        click HomoeologyTextMining href "../HomoeologyTextMining"
      TextMiningAnnotation <|-- HomologyTextMining
        click HomologyTextMining href "../HomologyTextMining"
      TextMiningAnnotation <|-- HomIntTextMining
        click HomIntTextMining href "../HomIntTextMining"
      TextMiningAnnotation <|-- SeqSimTextMining
        click SeqSimTextMining href "../SeqSimTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [AnnotationMethod](AnnotationMethod.md)
        * **TextMiningAnnotation** [ [ComputationallyInferredAssociation](ComputationallyInferredAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [RegulationTextMining](RegulationTextMining.md) | An association that represents a text mining annotation based on gene express... |
| [PhysInteractTextMining](PhysInteractTextMining.md) | An association that represents a text mining annotation based on physical int... |
| [GeneIntTextMining](GeneIntTextMining.md) | An association that represents a text mining annotation based on gene-gene in... |
| [HomoeologyTextMining](HomoeologyTextMining.md) | An association that represents a text mining annotation based on homoeology |
| [HomologyTextMining](HomologyTextMining.md) | An association that represents a text mining annotation based on homology |
| [HomIntTextMining](HomIntTextMining.md) | An association that represents a text mining annotation based on homology int... |
| [SeqSimTextMining](SeqSimTextMining.md) | An association that represents a text mining annotation based on sequence sim... |








## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:TextMiningAnnotation |
| native | motif:TextMiningAnnotation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextMiningAnnotation
description: 'An association that was computed via text mining methods, such as name-entity
  recognition,

  semantic similarity or LLM-based embeddings.

  '
title: Text Mining Annotation
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AnnotationMethod
abstract: true
mixin: true
mixins:
- ComputationallyInferredAssociation

```
</details>

### Induced

<details>
```yaml
name: TextMiningAnnotation
description: 'An association that was computed via text mining methods, such as name-entity
  recognition,

  semantic similarity or LLM-based embeddings.

  '
title: Text Mining Annotation
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AnnotationMethod
abstract: true
mixin: true
mixins:
- ComputationallyInferredAssociation

```
</details>