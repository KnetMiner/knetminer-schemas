

# Class: Manual Annotation (ManualAnnotation) 


_An association category that represents a manual annotation, provided by a curator or expert._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:ManualAnnotation](https://knetminer.com/terms/motifs/motif-categories/ManualAnnotation)






```mermaid
 classDiagram
    class ManualAnnotation
    click ManualAnnotation href "../ManualAnnotation"
      ManualAnnotationMethod <|-- ManualAnnotation
        click ManualAnnotationMethod href "../ManualAnnotationMethod"
      AnnotationMethod <|-- ManualAnnotation
        click AnnotationMethod href "../AnnotationMethod"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [AnnotationMethod](AnnotationMethod.md)
        * **ManualAnnotation** [ [ManualAnnotationMethod](ManualAnnotationMethod.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | direct::annotation |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:ManualAnnotation |
| native | motif:ManualAnnotation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ManualAnnotation
annotations:
  originalCategory:
    tag: originalCategory
    value: direct::annotation
description: 'An association category that represents a manual annotation, provided
  by a curator or expert.

  '
title: Manual Annotation
notes:
- 'original category no: 1.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AnnotationMethod
abstract: true
mixins:
- ManualAnnotationMethod

```
</details>

### Induced

<details>
```yaml
name: ManualAnnotation
annotations:
  originalCategory:
    tag: originalCategory
    value: direct::annotation
description: 'An association category that represents a manual annotation, provided
  by a curator or expert.

  '
title: Manual Annotation
notes:
- 'original category no: 1.1'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: AnnotationMethod
abstract: true
mixins:
- ManualAnnotationMethod

```
</details>