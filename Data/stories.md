## Story 01
* greet
  - utter_greet
 
## Story 02
* bye
  - utter_bye

## Story 03
* inform_general_statistics
  - action_general_stat

## Story 04
* reveal_dataset
  - action_get_obs
  - action_get_var
  - action_get_analysis_type
  
## Story 05
* how_to_intepret
  - action_access_db

## Story 06
* what_is
  - action_access_db

## Story 07
* how_to_apply
  - action_access_db

## Story 08
* assess_accuracy_model
  - action_access_db

## Story 09
* diagnostics
  - action_access_db

## Story 10
* model_selection_methods
  - action_access_db

## Story 11
* use_categorical_variables
  - action_access_db

## Story 12
* use_categorical_variables
  - action_access_db

## Story 13
* outliers
  - action_access_db

## Story 14
* Multicollinearity
  - action_access_db

## Story 15
* improve_accuracy
  - action_access_db

## Story 16
* Assumptions
  - action_access_db

## Story 17
* non_linear_relationships
  - action_access_db

## Story 18
* summarise
  - action_access_data_science

## Story 18
* filter
  - action_access_data_science

## Story 18
* group_by
  - action_access_data_science

## fallback story
* wrong_spellings
  - action_default_fallback

## Generated Story -3271213933342323996
* greet
    - utter_greet
* inform_general_statistics
* informGeneralStatistics{"statTerm": "statistics"}
    - slot{"statTerm": "statistics"}
    - action_general_stat
    - slot{"statTerm": "statistics"}
* reveal_dataset
    - action_get_obs
    - slot{"num_observations": 1200}
    - action_get_var
    - slot{"num_variables": 12}
    - action_get_analysis_type
    - slot{"default_ml_type": "multiple regression"}
* what_is{"given_ml": "multiple regression"}
    - slot{"given_ml": "multiple regression"}
    - action_access_db
    - slot{"given_ml": null}
* how_to_intepret{"given_ml": "random forest"}
    - slot{"given_ml": "random forest"}
* how_to_apply{"given_ml": "random forest"}
    - slot{"given_ml": "random forest"}
    - action_access_db
    - slot{"given_ml": null}
    - export



