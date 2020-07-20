import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * GeneToExpressionSiteAssociation
 * <p>
 * An association between a gene and an expression site, possibly qualified by stage/timing info.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object",
    "quantifier_qualifier",
    "relation",
    "stage_qualifier",
    "subject"
})
public class GeneToExpressionSiteAssociation {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    private String object;
    @JsonProperty("quantifier_qualifier")
    private String quantifierQualifier;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    private String relation;
    @JsonProperty("stage_qualifier")
    private String stageQualifier;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    @JsonProperty("quantifier_qualifier")
    public String getQuantifierQualifier() {
        return quantifierQualifier;
    }

    @JsonProperty("quantifier_qualifier")
    public void setQuantifierQualifier(String quantifierQualifier) {
        this.quantifierQualifier = quantifierQualifier;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    @JsonProperty("stage_qualifier")
    public String getStageQualifier() {
        return stageQualifier;
    }

    @JsonProperty("stage_qualifier")
    public void setStageQualifier(String stageQualifier) {
        this.stageQualifier = stageQualifier;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(GeneToExpressionSiteAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("object");
        sb.append('=');
        sb.append(((this.object == null)?"<null>":this.object));
        sb.append(',');
        sb.append("quantifierQualifier");
        sb.append('=');
        sb.append(((this.quantifierQualifier == null)?"<null>":this.quantifierQualifier));
        sb.append(',');
        sb.append("relation");
        sb.append('=');
        sb.append(((this.relation == null)?"<null>":this.relation));
        sb.append(',');
        sb.append("stageQualifier");
        sb.append('=');
        sb.append(((this.stageQualifier == null)?"<null>":this.stageQualifier));
        sb.append(',');
        sb.append("subject");
        sb.append('=');
        sb.append(((this.subject == null)?"<null>":this.subject));
        sb.append(',');
        if (sb.charAt((sb.length()- 1)) == ',') {
            sb.setCharAt((sb.length()- 1), ']');
        } else {
            sb.append(']');
        }
        return sb.toString();
    }

    @Override
    public int hashCode() {
        int result = 1;
        result = ((result* 31)+((this.stageQualifier == null)? 0 :this.stageQualifier.hashCode()));
        result = ((result* 31)+((this.quantifierQualifier == null)? 0 :this.quantifierQualifier.hashCode()));
        result = ((result* 31)+((this.subject == null)? 0 :this.subject.hashCode()));
        result = ((result* 31)+((this.object == null)? 0 :this.object.hashCode()));
        result = ((result* 31)+((this.relation == null)? 0 :this.relation.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneToExpressionSiteAssociation) == false) {
            return false;
        }
        GeneToExpressionSiteAssociation rhs = ((GeneToExpressionSiteAssociation) other);
        return ((((((this.stageQualifier == rhs.stageQualifier)||((this.stageQualifier!= null)&&this.stageQualifier.equals(rhs.stageQualifier)))&&((this.quantifierQualifier == rhs.quantifierQualifier)||((this.quantifierQualifier!= null)&&this.quantifierQualifier.equals(rhs.quantifierQualifier))))&&((this.subject == rhs.subject)||((this.subject!= null)&&this.subject.equals(rhs.subject))))&&((this.object == rhs.object)||((this.object!= null)&&this.object.equals(rhs.object))))&&((this.relation == rhs.relation)||((this.relation!= null)&&this.relation.equals(rhs.relation))));
    }

}
