{% macro generate_purchase_types(field, types) %}
    case
        {% for purchase_type, match_criteria in types.items() %}
            {% set match_len = match_criteria.match | length %}
            {% set non_match_len = match_criteria.non_match | length %}
            {% if match_len > 0 %}
                when
                    {% for criteria in match_criteria.match %}
                        {% if loop.last and non_match_len == 0%}
                            regexp_matches({{ field }},'{{ criteria }}', 'i')
                        {% else %}
                            regexp_matches({{ field }},'{{ criteria }}', 'i') and
                        {% endif %}
                    {% endfor %}
                    {% for criteria in match_criteria.non_match %}
                        {% if loop.last %}
                            not regexp_matches({{ field }}, '{{ criteria }}', 'i')
                        {% else %}
                            not regexp_matches({{ field }}, '{{ criteria }}', 'i') and
                        {% endif %}
                    {% endfor %}
                then
                    '{{ purchase_type }}'
            {% endif %}
        {% endfor %}
    end
{% endmacro %}