package naram.kim.recruit.model;

import java.sql.*;
import java.util.ArrayList;

public class RecruitmentDAO {
	
	private static RecruitmentDAO dao = new RecruitmentDAO();

	private RecruitmentDAO() {
		
		try {
			Class.forName("com.mysql.jdbc.Driver");
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
	//외부로부터 접근 가능한 public 메서드로 객체를 return
  
	public static RecruitmentDAO getInstance() {
		if(dao == null) { //안전장치
			dao = new RecruitmentDAO();
		}
		return dao;
	}
	
	String url = "jdbc:mysql://ec2-52-55-98-182.compute-1.amazonaws.com/Crawler";
	String user = "cloud";
	String upw = "1111";
	
	Connection conn = null;
	PreparedStatement pstmt = null;
	Statement stmt = null;
	ResultSet rs = null;
	
	public ArrayList<RecruitmentVO> listRecruitment(int from, int to) {
		
		ArrayList<RecruitmentVO> list = new ArrayList<>();
		
		String sql = "select * from re_info where id >= ? and id <= ?";
		
		try {
			
			conn = DriverManager.getConnection(url,user,upw);
			
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setInt(1, from);
			pstmt.setInt(2, to);
			
			rs = pstmt.executeQuery(); // executeQuery()를 통해 select문 실행
			
			while(rs.next()) {
				
				String company = rs.getString(1);
				String title = rs.getString(2);
				String titlelink = rs.getString(3);
				String site_name = rs.getString(4);
				String field1 = rs.getString(5);
				String field2 = rs.getString(6);
				String field3 = rs.getString(7);
				String career = rs.getString(8);
				String academic = rs.getString(9);
				String area = rs.getString(10);
				String workingcondition = rs.getString(11);
				String deadline = rs.getString(12);
				
				RecruitmentVO vo = new RecruitmentVO(company, title, titlelink, site_name, field1
						, field2, field3, career, academic, area, workingcondition, deadline);
				
				list.add(vo);
			}
			
		} catch (Exception e) {
			 
			e.printStackTrace();
		
		} finally {
				
				try {
					
				if(conn != null) conn.close();
				if(pstmt != null) pstmt.close();
				if(rs != null) rs.close();
				
			} catch (Exception e2) {
				
				e2.printStackTrace();
				
			}

		}
		
		return list;
	}
	
	public ArrayList<RecruitmentVO> searchRecruitment(String search) {
		
		ArrayList<RecruitmentVO> list = new ArrayList<>();
		
		String sql = "select * from re_info where company like ? or title like ?";
		 
		
		try {
			conn = DriverManager.getConnection(url,user,upw);
			
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, "%"+search+"%");
			pstmt.setString(2, "%"+search+"%");
			
			rs = pstmt.executeQuery(); // executeQuery()를 통해 select문 실행
			
			while(rs.next()) {
				
				String company = rs.getString(1);
				String title = rs.getString(2);
				String titlelink = rs.getString(3);
				String site_name = rs.getString(4);
				String field1 = rs.getString(5);
				String field2 = rs.getString(6);
				String field3 = rs.getString(7);
				String career = rs.getString(8);
				String academic = rs.getString(9);
				String area = rs.getString(10);
				String workingcondition = rs.getString(11);
				String deadline = rs.getString(12);
				
				RecruitmentVO vo = new RecruitmentVO(company, title, titlelink, site_name, field1
						, field2, field3, career, academic, area, workingcondition, deadline);
				
				list.add(vo);
			}
		} catch (Exception e) {
				 
				e.printStackTrace();
			
			} finally {
					
					try {
						
					if(conn != null) conn.close();
					if(pstmt != null) pstmt.close();
					if(rs != null) rs.close();
					
				} catch (Exception e2) {
					
					e2.printStackTrace();
					
				}

			}
			
			return list;		
	}
	
	public int RecruitmentTotal() {
		
		String sql = "select id from re_info";
		int total = 0;
		 
		
		try {
			
			conn = DriverManager.getConnection(url,user,upw);
			
			pstmt = conn.prepareStatement(sql);
			
			rs = pstmt.executeQuery(); // executeQuery()를 통해 select문 실행
			
			while(rs.next()) {
				
				total = total + 1;
				
			}
		} catch (Exception e) {
				 
				e.printStackTrace();
			
			} finally {
					
					try {
						
					if(conn != null) conn.close();
					if(pstmt != null) pstmt.close();
					if(rs != null) rs.close();
					
				} catch (Exception e2) {
					
					e2.printStackTrace();
					
				}

			}
			
			return total;		
	}
	
}