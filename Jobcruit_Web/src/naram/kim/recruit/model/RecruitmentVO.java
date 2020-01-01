package naram.kim.recruit.model;

import java.sql.Date;

public class RecruitmentVO {

	private String company;
	private String title;
	private String titlelink;
	private String site_name;
	private String field1;
	private String field2;
	private String field3;
	private String career;
	private String academic; 
	private String area;
	private String workingcondition;
	private String deadline;
	
	public RecruitmentVO() { // 생성자
		
	}
	
	public RecruitmentVO(String company, String title, String titlelink, String site_name, String field1, String field2, String field3
			, String career, String academic, String area, String workingcondition, String deadline) {
		super();
		
		this.company = company;
		this.title = title;
		this.titlelink = titlelink;
		this.site_name = site_name;
		this.field1 = field1;
		this.field2 = field2;
		this.field3 = field3;
		this.career = career;
		this.academic = academic;
		this.area = area;
		this.workingcondition = workingcondition;
		this.deadline = deadline;
		
	} // 생성자
	
	public String getCompany() {
		return company;
	}

	public void setCompany(String company) {
		this.company = company;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getTitlelink() {
		return titlelink;
	}

	public void setTitlelink(String titlelink) {
		this.titlelink = titlelink;
	}

	public String getSite_name() {
		return site_name;
	}

	public void setSite_name(String site_name) {
		this.site_name = site_name;
	}

	public String getField1() {
		return field1;
	}

	public void setField1(String field1) {
		this.field1 = field1;
	}

	public String getField2() {
		return field2;
	}

	public void setField2(String field2) {
		this.field2 = field2;
	}

	public String getField3() {
		return field3;
	}

	public void setField3(String field3) {
		this.field3 = field3;
	}

	public String getCareer() {
		return career;
	}

	public void setCareer(String career) {
		this.career = career;
	}

	public String getAcademic() {
		return academic;
	}

	public void setAcademic(String academic) {
		this.academic = academic;
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
		this.area = area;
	}

	public String getWorkingcondition() {
		return workingcondition;
	}

	public void setWorkingcondition(String workingcondition) {
		this.workingcondition = workingcondition;
	}

	public String getDeadline() {
		return deadline;
	}

	public void setDeadline(String deadline) {
		this.deadline = deadline;
	}

}