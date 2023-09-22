-- analyses/my_analysis.sql

-- Import the macro from the dbt_utils package

-- Use the macro
SELECT
    
    case
        
            
            
            
                when
                    
                        
                            regexp_matches(description,'.*swiggy.*', 'i') and
                        
                    
                    
                        
                            not regexp_matches(description, '.*instamart.*', 'i')
                        
                    
                then
                    'swiggy'
            
        
            
            
            
                when
                    
                        
                            regexp_matches(description,'.*instamart.*', 'i')
                        
                    
                    
                then
                    'instamart'
            
        
            
            
            
                when
                    
                        
                            regexp_matches(description,'.*supermarket.*', 'i')
                        
                    
                    
                then
                    'supermarket'
            
        
            
            
            
                when
                    
                        
                            regexp_matches(description,'.*big.*', 'i') and
                        
                    
                        
                            regexp_matches(description,'.*basket.*', 'i')
                        
                    
                    
                then
                    'bigbasket'
            
        
    end
 AS status_label
FROM
    my_table