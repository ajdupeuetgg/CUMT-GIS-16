
// MDrawView.h : CMDrawView ��Ľӿ�
//

#pragma once


class CMDrawView : public CView
{
protected:
	// �������л�����
	CMDrawView();
	DECLARE_DYNCREATE(CMDrawView)

// ����
public:
	CMDrawDoc* GetDocument() const;

// ����
public:

// ��д
public:
	virtual void OnDraw(CDC* pDC);  // ��д�Ի��Ƹ���ͼ
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
protected:
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);

// ʵ��
public:
	virtual ~CMDrawView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

	int PushNumb; //������¼�����������Ĵ���
	int m_DrawCurrent;//������¼���ڵĲ������
	CPoint m_bO; // Բ��
	CPoint m_bR; //Բ�ϵĵ�
	int m_ist; //Բ����Բ���ϵ������m_ist=0����ʾ��������ΪԲ�ģ�
			   //m_ist=1����ʾ��������ΪԲ���ϵĵ�
	CPoint m_rO;
	CPoint m_rR;
	int mR_ist;
	bool curveFlag;

	COLORREF m_color;  //ȫ����ɫ
	int penStyle;   //������
	int penWidth;   //�߿�

	int m_iPolyDotNumbers;//����ζ������(�ߵĸ���)

	CPoint m_ptPolyDotArrays[999];//�洢����εĶ���

	CBrush greenBr;
	CBrush redBr;
	CBrush blueBr;


	struct myFont  //������Ϣ�ṹ��
	{
		CFont newFont;
		CFont* oldFont;
		CString text;
		int size;
		CString faceName;
	}m_font;
private:
	CPoint mPointOrign, mPointOld;


	// ���ɵ���Ϣӳ�亯��
protected:
	afx_msg void OnFilePrintPreview();
	//	afx_msg void OnRButtonUp(UINT nFlags, CPoint point);
	afx_msg void OnContextMenu(CWnd* pWnd, CPoint point);
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnDrawLine();
	afx_msg void OnDrawPline();
	void drawCircle(CClientDC* pDC, CPoint cenp, CPoint ardp);
	int computeRadius(CPoint cenp, CPoint ardp);
	afx_msg void OnDrawCircle();
	afx_msg void OnDrawRectangle();
	void testCircle(CDC* pDC, CPoint cenp, CPoint ardp);
	void drawRect(CClientDC* ht, CPoint cPoint, CPoint ePoint);
	afx_msg void OnInsertText();
	void drawText(CClientDC* ht, CPoint curPoint, CString text);
	afx_msg void OnColorBlack();
	afx_msg void OnColorRed();
	afx_msg void OnColorGreen();
	afx_msg void OnColorBlue();
	afx_msg void OnColorCustom();
	afx_msg void OnPenstyleSolid();
	afx_msg void OnPanstyleDash();
	afx_msg void OnPanstyleDot();
	afx_msg void OnPanstyleDashdot();
	afx_msg void OnPanstyleDashdotdot();
	afx_msg void OnPenwidthThin();
	afx_msg void OnPenwidthMid();
	afx_msg void OnPenwidthThick();
	afx_msg void OnPenwidthCustom();
	afx_msg void OnDrawPolygon();
	void drawCurve(CClientDC* ht, CPoint first, CPoint second);
	afx_msg void OnDrawCustom();
	afx_msg void OnLine();
	afx_msg void OnRectangle();
	afx_msg void OnCircle();
	afx_msg void OnLButtonUp(UINT nFlags, CPoint point);
	afx_msg void OnLButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnMouseMove(UINT nFlags, CPoint point);
	afx_msg void OnPaint();
	afx_msg void OnRButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnEraseAll();
	afx_msg void OnEraseCu();
	afx_msg BOOL OnSetCursor(CWnd* pWnd, UINT nHitTest, UINT message);
	afx_msg void OnDrawCu();
	afx_msg void ChangePenBlue();
	afx_msg void ChangePenBlack();
	afx_msg void ChangePenRed();
	afx_msg void ChangePenGreen();
};

#ifndef _DEBUG  // MDrawView.cpp �еĵ��԰汾
inline CMDrawDoc* CMDrawView::GetDocument() const
   { return reinterpret_cast<CMDrawDoc*>(m_pDocument); }
#endif

