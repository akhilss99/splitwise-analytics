with purchases as (
    select 
        month,
        year,
        group_name,
        description,
        cost,
        date,
        category,
        
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
 as purchase_type
    from
        "analyticsdb"."main_intermediate"."fact_group_expenditures"
    where 
        purchase_type is not null
)

select * from purchases