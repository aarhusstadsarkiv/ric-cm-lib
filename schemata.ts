// noinspection JSUnusedLocalSymbols,JSUnusedGlobalSymbols

export type FreeText = string
export type ModelBasedText = `model:${string}:${string}`
export type RuleBasedText = `rule:${string}:${string}`

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
        demographic_group: ControlledValues.DemographicGroup  // https://www.ica.org/standards/RiC/ontology±#DemographicGroup
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
    relation_type: Relations.RelationType
    domain_type: Things.EntityDomain | "Relation"
    domain_identifier: string
    target_type: Things.EntityDomain | "Relation"
    target_identifier: string
  }

  export enum RelationType {
    R001 = 1,
    R002 = 2,
    R002i = -2,
    R003 = 3,
    R003i = -3,
    R004 = 4,
    R004i = -4,
    R005 = 5,
    R005i = -5,
    R006 = 6,
    R006i = -6,
    R007 = 7,
    R007i = -7,
    R008 = 8,
    R008i = -8,
    R009 = 9,
    R009i = -9,
    R010 = 10,
    R010i = -10,
    R011 = 11,
    R011i = -11,
    R012 = 12,
    R012i = -12,
    R013 = 13,
    R013i = -13,
    R014 = 14,
    R014i = -14,
    R015 = 15,
    R015i = -15,
    R016 = 16,
    R016i = -16,
    R017 = 17,
    R017i = -17,
    R018 = 18,
    R018i = -18,
    R019 = 19,
    R019i = -19,
    R020 = 20,
    R020i = -20,
    R021 = 21,
    R021i = -21,
    R022 = 22,
    R023 = 23,
    R024 = 24,
    R024i = -24,
    R025 = 25,
    R025i = -25,
    R026 = 26,
    R026i = -26,
    R027 = 27,
    R027i = -27,
    R028 = 28,
    R028i = -28,
    R029 = 29,
    R029i = -29,
    R030 = 30,
    R030i = -30,
    R031 = 31,
    R031i = -31,
    R032 = 32,
    R032i = -32,
    R033 = 33,
    R033i = -33,
    R034 = 34,
    R035 = 35,
    R036 = 36,
    R036i = -36,
    R037 = 37,
    R037i = -37,
    R038 = 38,
    R038i = -38,
    R039 = 39,
    R039i = -39,
    R040 = 40,
    R040i = -40,
    R041 = 41,
    R041i = -41,
    R042 = 42,
    R042i = -42,
    R044 = 44,
    R045 = 45,
    R045i = -45,
    R046 = 46,
    R047 = 47,
    R048 = 48,
    R049 = 49,
    R050 = 50,
    R050i = -50,
    R051 = 51,
    R052 = 52,
    R053 = 53,
    R053i = -53,
    R054 = 54,
    R054i = -54,
    R055 = 55,
    R055i = -55,
    R056 = 56,
    R056i = -56,
    R057 = 57,
    R057i = -57,
    R058 = 58,
    R058i = -58,
    R059 = 59,
    R059i = -59,
    R060 = 60,
    R060i = -60,
    R061 = 61,
    R061i = -61,
    R062 = 62,
    R062i = -62,
    R063 = 63,
    R063i = -63,
    R064 = 64,
    R064i = -64,
    R065 = 65,
    R065i = -65,
    R066 = 66,
    R066i = -66,
    R067 = 67,
    R067i = -67,
    R068 = 68,
    R068i = -68,
    R069 = 69,
    R069i = -69,
    R070 = 70,
    R070i = -70,
    R071 = 71,
    R071i = -71,
    R072 = 72,
    R072i = -72,
    R073 = 73,
    R073i = -73,
    R074 = 74,
    R074i = -74,
    R075 = 75,
    R075i = -75,
    R076 = 76,
    R076i = -76,
    R077 = 77,
    R078 = 78,
    R079 = 79,
    R079i = -79,
  }
}
