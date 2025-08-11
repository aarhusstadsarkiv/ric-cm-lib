// noinspection JSUnusedLocalSymbols,JSUnusedGlobalSymbols

type FreeText = string
type ModelBasedText = `model:${string}:${string}`
type RuleBasedText = `rule:${string}:${string}`

export namespace Things {
  export interface Thing {
    id: string // internal ID
    identifier: FreeText | ModelBasedText | RuleBasedText  // https://www.ica.org/standards/RiC/ontology#identifier
    name: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#name
    general_description: FreeText  // https://www.ica.org/standards/RiC/ontology#generalDescription
  }

  export namespace RecordsResources {
    export interface RecordResource extends Thing {
      authenticity_note: FreeText | ModelBasedText | null  // https://www.ica.org/standards/RiC/ontology#authenticityNote
      classification: ControlledValues.ClassificationType | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#classification
      conditions_of_access: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#conditionsOfAccess
      conditions_of_use: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#conditionsOfUse
      content_type: ControlledValues.ContentType  // https://www.ica.org/standards/RiC/ontology#ContentType
      history: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#history
      integrity_note: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#integrityNote
      language: ControlledValues.Language  // https://www.ica.org/standards/RiC/ontology#Language
      legal_status: ControlledValues.LegalStatus  // https://www.ica.org/standards/RiC/ontology#LegalStatus
      record_resource_extent: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#recordResourceExtent
      scope_and_content: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#scopeAndContent
      state: ControlledValues.RecordState  // https://www.ica.org/standards/RiC/ontology#RecordState
      structure: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#structure
    }

    export interface RecordSet extends RecordResource {
      accruals: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#accruals
      record_set_type: ControlledValues.RecordSetType  // https://www.ica.org/standards/RiC/ontology#RecordSetType
    }

    export interface Record extends RecordResource {
      documentary_form_type: ControlledValues.DocumentaryFormType  // https://www.ica.org/standards/RiC/ontology#DocumentaryFormType
    }

    export interface RecordPart extends RecordResource {
      documentary_form_type: ControlledValues.DocumentaryFormType  // https://www.ica.org/standards/RiC/ontology#DocumentaryFormType
    }
  }

  export namespace Instantiations {
    export interface Instantiation extends Thing {
      authenticity_note: FreeText | ModelBasedText | null  // https://www.ica.org/standards/RiC/ontology#authenticityNote
      carrier_extent: FreeText | ModelBasedText | null // https://www.ica.org/standards/RiC/ontology#CarrierExtent
      carrier_type: ControlledValues.CarrierType  // https://www.ica.org/standards/RiC/ontology#CarrierType
      conditions_of_access: FreeText | ModelBasedText
      conditions_of_use: FreeText | ModelBasedText
      history: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#history
      instantiation_extent: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#instantiationExtent
      physical_characteristics_note: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#physicalCharacteristicsNote
      production_technique: FreeText | ControlledValues.ProductionTechnique  // https://www.ica.org/standards/RiC/ontology#productionTechnique
      quality_of_representation_note: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#qualityOfRepresentationNote
      representation_type: ControlledValues.RepresentationType  // https://www.ica.org/standards/RiC/ontology#RepresentationType
      structure: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#instantiationStructure
    }
  }

  export namespace Agents {
    export interface Agent extends Thing {
      history: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#history
      language: ControlledValues.Language  // https://www.ica.org/standards/RiC/ontology#Language
      legal_status: ControlledValues.LegalStatus  // https://www.ica.org/standards/RiC/ontology#LegalStatus
    }

    export interface Person extends Agent {
      demographic_group: ControlledValues.DemographicGroup  // https://www.ica.org/standards/RiC/ontology#DemographicGroup
      occupation_type: ControlledValues.OccupationType  // https://www.ica.org/standards/RiC/ontology#OccupationType
    }

    export interface Position extends Agent {
    }

    export interface Mechanism extends Agent {
      technical_characteristics: FreeText  // https://www.ica.org/standards/RiC/ontology#technicalCharacteristics
    }

    export namespace Groups {
      export interface Group extends Agent {
        demographic_group: ControlledValues.DemographicGroup  // https://www.ica.org/standards/RiC/ontology#
        occupation_type: string  // https://www.ica.org/standards/RiC/ontology#
      }

      export interface Family extends Group {
        family_type: ControlledValues.FamilyType  // https://www.ica.org/standards/RiC/ontology#FamilyType
      }

      export interface CorporateBody extends Group {
        corporate_body_type: ControlledValues.CorporateBodyType  // https://www.ica.org/standards/RiC/ontology#CorporateBodyType
      }
    }
  }

  export namespace Events {
    export interface Event extends Thing {
      event_type: ControlledValues.EventType  // https://www.ica.org/standards/RiC/ontology#EventType
      history: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#history
    }

    export interface Activity extends Event {
      activity_type: ControlledValues.ActivityType  // https://www.ica.org/standards/RiC/ontology#ActivityType
    }
  }

  export namespace Rules {
    export interface Rule extends Thing {
      history: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#
      rule_type: ControlledValues.RuleType  // https://www.ica.org/standards/RiC/ontology#RuleType
    }

    export interface Mandate extends Rule {
      mandate_type: ControlledValues.MandateType  // https://www.ica.org/standards/RiC/ontology#MandateType
    }
  }

  export namespace Dates {
    export interface Date extends Thing {
      date_qualifier: ControlledValues.DateQualifier  // https://www.ica.org/standards/RiC/ontology#dateQualifier
      date_type: ControlledValues.DateType  // https://www.ica.org/standards/RiC/ontology#DateType
      expressed_date: ModelBasedText  // https://www.ica.org/standards/RiC/ontology#expressedDate
      normalized_date: RuleBasedText  // https://www.ica.org/standards/RiC/ontology#normalizedDateValue
    }
  }

  export namespace Places {
    export interface Place extends Thing {
      coordinates: { latitude: number; longitude: number, height: number | null, standard: string | null }  // https://www.ica.org/standards/RiC/ontology#Coordinates
      history: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#history
      location: FreeText  // https://www.ica.org/standards/RiC/ontology#location
      place_type: ControlledValues.PlaceType  // https://www.ica.org/standards/RiC/ontology#PlaceType
    }
  }

  export type EntityDomain =
    "RecordSet"
    | "Record"
    | "RecordPart"
    | "Instantiation"
    | "Person"
    | "Position"
    | "Mechanism"
    | "Family"
    | "CorporateBody"
    | "Event"
    | "Activity"
    | "Rule"
    | "Mandate"
    | "Date"
    | "Place"
}

export namespace ControlledValues {
  export enum PlaceType {
    // https://www.ica.org/standards/RiC/ontology#PlaceType
  }

  export enum DateQualifier {
    // https://www.ica.org/standards/RiC/ontology#dateQualifier
  }

  export enum DateType {
    // https://www.ica.org/standards/RiC/ontology#DateType
  }

  export enum MandateType {
    // https://www.ica.org/standards/RiC/ontology#MandateType
  }

  export enum RuleType {
    // https://www.ica.org/standards/RiC/ontology#RuleType
  }

  export enum ActivityType {
    // https://www.ica.org/standards/RiC/ontology#ActivityType
  }

  export enum EventType {
    // https://www.ica.org/standards/RiC/ontology#EventType
  }

  export enum CarrierType {
    // https://www.ica.org/standards/RiC/ontology#CarrierType
  }

  export enum ProductionTechnique {
    // https://www.ica.org/standards/RiC/ontology#productionTechnique
  }

  export enum RepresentationType {
    // https://www.ica.org/standards/RiC/ontology#RepresentationType
  }

  export enum ClassificationType {
    // https://www.ica.org/standards/RiC/ontology#classification
  }

  export enum ContentType {
    // https://www.ica.org/standards/RiC/ontology#ContentType
  }

  export enum DocumentaryFormType {
    // https://www.ica.org/standards/RiC/ontology#DocumentaryFormType
  }

  export enum Language {
    // https://www.ica.org/standards/RiC/ontology#Language
  }

  export enum LegalStatus {
    // https://www.ica.org/standards/RiC/ontology#LegalStatus
  }

  export enum RecordSetType {
    // https://www.ica.org/standards/RiC/ontology#RecordSetType
  }

  export enum RecordState {
    // https://www.ica.org/standards/RiC/ontology#RecordState
  }

  export enum DemographicGroup {
    // https://www.ica.org/standards/RiC/ontology#DemographicGroup
  }

  export enum OccupationType {
    // https://www.ica.org/standards/RiC/ontology#OccupationType
  }

  export enum CorporateBodyType {
    // https://www.ica.org/standards/RiC/ontology#CorporateBodyType
  }

  export enum FamilyType {
    // https://www.ica.org/standards/RiC/ontology#FamilyType
  }
}

export namespace Relations {
  export interface Relation {
    certainty_of_relation: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#relationCertainty
    date_of_relation: FreeText | ModelBasedText | RuleBasedText // RA02
    description_of_relation: FreeText  // RA03
    identifier_of_relation: FreeText | ModelBasedText | RuleBasedText  // RA04
    source_of_relation: FreeText | ModelBasedText  // https://www.ica.org/standards/RiC/ontology#relationSource
    place_of_relation: string  // RA06

    id: string
    type: Relations.Type
    domain_type: Things.EntityDomain
    domain_id: string
    target_type: Things.EntityDomain
    target_id: string
  }

  export enum Type {
    R001 = 0x1,
    R002 = 0x2,
    R002i = 0x5a,
    R003 = 0x3,
    R003i = 0x7e,
    R004 = 0x4,
    R004i = 0xa2,
    R005 = 0x5,
    R005i = 0xc6,
    R006 = 0x6,
    R006i = 0xea,
    R007 = 0x7,
    R007i = 0x10e,
    R008 = 0x8,
    R008i = 0x132,
    R009 = 0x9,
    R009i = 0x156,
    R010 = 0x24,
    R010i = 0x522,
    R011 = 0x25,
    R011i = 0x546,
    R012 = 0x26,
    R012i = 0x56a,
    R013 = 0x27,
    R013i = 0x58e,
    R014 = 0x28,
    R014i = 0x5b2,
    R015 = 0x29,
    R015i = 0x5d6,
    R016 = 0x2a,
    R016i = 0x5fa,
    R017 = 0x2b,
    R017i = 0x61e,
    R018 = 0x2c,
    R018i = 0x642,
    R019 = 0x2d,
    R019i = 0x666,
    R020 = 0x48,
    R020i = 0xa32,
    R021 = 0x49,
    R021i = 0xa56,
    R022 = 0x4a,
    R023 = 0x4b,
    R024 = 0x4c,
    R024i = 0xac2,
    R025 = 0x4d,
    R025i = 0xae6,
    R026 = 0x4e,
    R026i = 0xb0a,
    R027 = 0x4f,
    R027i = 0xb2e,
    R028 = 0x50,
    R028i = 0xb52,
    R029 = 0x51,
    R029i = 0xb76,
    R030 = 0x6c,
    R030i = 0xf42,
    R031 = 0x6d,
    R031i = 0xf66,
    R032 = 0x6e,
    R032i = 0xf8a,
    R033 = 0x6f,
    R033i = 0xfae,
    R034 = 0x70,
    R035 = 0x71,
    R036 = 0x72,
    R036i = 0x101a,
    R037 = 0x73,
    R037i = 0x103e,
    R038 = 0x74,
    R038i = 0x1062,
    R039 = 0x75,
    R039i = 0x1086,
    R040 = 0x90,
    R040i = 0x1452,
    R041 = 0x91,
    R041i = 0x1476,
    R042 = 0x92,
    R042i = 0x149a,
    R044 = 0x94,
    R045 = 0x95,
    R045i = 0x1506,
    R046 = 0x96,
    R047 = 0x97,
    R048 = 0x98,
    R049 = 0x99,
    R050 = 0xb4,
    R050i = 0x1962,
    R051 = 0xb5,
    R052 = 0xb6,
    R053 = 0xb7,
    R053i = 0x19ce,
    R054 = 0xb8,
    R054i = 0x19f2,
    R055 = 0xb9,
    R055i = 0x1a16,
    R056 = 0xba,
    R056i = 0x1a3a,
    R057 = 0xbb,
    R057i = 0x1a5e,
    R058 = 0xbc,
    R058i = 0x1a82,
    R059 = 0xbd,
    R059i = 0x1aa6,
    R060 = 0xd8,
    R060i = 0x1e72,
    R061 = 0xd9,
    R061i = 0x1e96,
    R062 = 0xda,
    R062i = 0x1eba,
    R063 = 0xdb,
    R063i = 0x1ede,
    R064 = 0xdc,
    R064i = 0x1f02,
    R065 = 0xdd,
    R065i = 0x1f26,
    R066 = 0xde,
    R066i = 0x1f4a,
    R067 = 0xdf,
    R067i = 0x1f6e,
    R068 = 0xe0,
    R068i = 0x1f92,
    R069 = 0xe1,
    R069i = 0x1fb6,
    R070 = 0xfc,
    R070i = 0x2382,
    R071 = 0xfd,
    R071i = 0x23a6,
    R072 = 0xfe,
    R072i = 0x23ca,
    R073 = 0xff,
    R073i = 0x23ee,
    R074 = 0x100,
    R074i = 0x2412,
    R075 = 0x101,
    R075i = 0x2436,
    R076 = 0x102,
    R076i = 0x245a,
    R077 = 0x103,
    R078 = 0x104,
    R079 = 0x105,
    R079i = 0x24c6,
  }
}
