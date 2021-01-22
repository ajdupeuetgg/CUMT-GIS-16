
// MDrawView.cpp : CMDrawView ���ʵ��
//

#include "stdafx.h"
// SHARED_HANDLERS ������ʵ��Ԥ��������ͼ������ɸѡ�������
// ATL ��Ŀ�н��ж��壬�����������Ŀ�����ĵ����롣
#ifndef SHARED_HANDLERS
#include "MDraw.h"
#endif

#include "MDrawDoc.h"
#include "MDrawView.h"
#include "MainFrm.h"



#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#define NULLMODE 0
#define LINEMODE 1
#define PLINEMODE 2
#define CIRCLEMODE 3
#define RECTMODE 4
#define TEXTMODE 5
#define POLYGONMODE 6
#define ERASEMODE 7
#define CURVEMODE 8

#define COLOR_BLACK RGB(0,0,0)
#define COLOR_RED RGB(197,31,31)
#define COLOR_GREEN RGB(6,128,67)
#define COLOR_BLUE RGB(0,90,171)

#define PEN_WIDTH_THIN 1
#define PEN_WIDTH_MID 3
#define PEN_WIDTH_THICK 7

// CMDrawView

IMPLEMENT_DYNCREATE(CMDrawView, CView)

BEGIN_MESSAGE_MAP(CMDrawView, CView)
	// ��׼��ӡ����
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CView::OnFilePrintPreview)
	ON_COMMAND(ID_32771, &CMDrawView::OnLine)
	ON_COMMAND(ID_32772, &CMDrawView::OnRectangle)
	ON_COMMAND(ID_32773, &CMDrawView::OnCircle)
	ON_WM_LBUTTONUP()
	ON_WM_LBUTTONDOWN()
	ON_WM_MOUSEMOVE()
	ON_WM_PAINT()
	ON_WM_RBUTTONDOWN()
	ON_COMMAND(ID_32777, &CMDrawView::OnEraseAll)
	ON_COMMAND(ID_32774, &CMDrawView::OnEraseCu)
	ON_WM_SETCURSOR()
	ON_COMMAND(ID_32775, &CMDrawView::OnDrawCu)
	ON_COMMAND(ID_32781, &CMDrawView::ChangePenBlue)
	ON_COMMAND(ID_32779, &CMDrawView::ChangePenBlack)
	ON_COMMAND(ID_32780, &CMDrawView::ChangePenRed)
	ON_COMMAND(ID_32782, &CMDrawView::ChangePenGreen)
END_MESSAGE_MAP()

// CMDrawView ����/����

CMDrawView::CMDrawView()
{
	// TODO: �ڴ˴���ӹ������
	m_bO.x = 0; m_bO.y = 0;
	m_bR.x = 0; m_bR.y = 0;
	PushNumb = 0;
	m_ist = 0;
	mR_ist = 0;
	m_color = COLOR_BLACK;
	penStyle = PS_SOLID;
	penWidth = 3;
	m_iPolyDotNumbers = 0;
	curveFlag = FALSE;
	greenBr.CreateSolidBrush(COLOR_GREEN);
	redBr.CreateSolidBrush(COLOR_RED);
	blueBr.CreateSolidBrush(COLOR_BLUE);
}

CMDrawView::~CMDrawView()
{
}

BOOL CMDrawView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: �ڴ˴�ͨ���޸�
	//  CREATESTRUCT cs ���޸Ĵ��������ʽ

	return CView::PreCreateWindow(cs);
}

// CMDrawView ����

void CMDrawView::OnDraw(CDC* /*pDC*/)
{
	CMDrawDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	// TODO: �ڴ˴�Ϊ����������ӻ��ƴ���
}


// CMDrawView ��ӡ

BOOL CMDrawView::OnPreparePrinting(CPrintInfo* pInfo)
{
	// Ĭ��׼��
	return DoPreparePrinting(pInfo);
}

void CMDrawView::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: ��Ӷ���Ĵ�ӡǰ���еĳ�ʼ������
}

void CMDrawView::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: ��Ӵ�ӡ����е��������
}


// CMDrawView ���

#ifdef _DEBUG
void CMDrawView::AssertValid() const
{
	CView::AssertValid();
}

void CMDrawView::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CMDrawDoc* CMDrawView::GetDocument() const // �ǵ��԰汾��������
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CMDrawDoc)));
	return (CMDrawDoc*)m_pDocument;
}
#endif //_DEBUG


// CMDrawView ��Ϣ�������


void CMDrawView::OnLine()
{
	PushNumb = 0;
	m_DrawCurrent = PLINEMODE;
	// TODO: �ڴ���������������
}


void CMDrawView::OnRectangle()
{
	mR_ist = 0;
	m_DrawCurrent = RECTMODE;
	// TODO: �ڴ���������������
}


void CMDrawView::OnCircle()
{
	m_ist = 0;
	m_DrawCurrent = CIRCLEMODE;
	// TODO: �ڴ���������������
}


void CMDrawView::OnLButtonUp(UINT nFlags, CPoint point)
{
	// TODO: �ڴ������Ϣ�����������/�����Ĭ��ֵ
	
	CView::OnLButtonUp(nFlags, point);
}


void CMDrawView::OnLButtonDown(UINT nFlags, CPoint point)
{
	// TODO: �ڴ������Ϣ�����������/�����Ĭ��ֵ
	CClientDC ht(this);
	CMainFrame* pMain = (CMainFrame*)AfxGetApp()->m_pMainWnd;
	CPen cPen;
	cPen.CreatePen(penStyle, penWidth, m_color);
	CPen *pOldPen = ht.SelectObject(&cPen);
	switch (m_DrawCurrent)
	{
	case LINEMODE:
		if (PushNumb == 0) {
			PushNumb++;
			mPointOrign = point;
			mPointOld = point;
			CString pointStr;
			UpdateData(TRUE);
			SetCapture();
		}
		else if (PushNumb == 1) {
			ht.MoveTo(mPointOrign);
			ht.LineTo(point);
			PushNumb = 0;
			CString pointInfo, mPointOrignStr, mPointOldStr;
			UpdateData(TRUE);
			ReleaseCapture();
		}
		break;
	case PLINEMODE:
		if (PushNumb == 0) {
			PushNumb++;
			mPointOrign = point;
			mPointOld = point;
			CString pointStr;
			UpdateData(TRUE);
			SetCapture();
		}
		else {
			ht.MoveTo(mPointOrign);
			ht.LineTo(point);
			mPointOrign = point;
			mPointOld = point;
			CString pointStr;
			UpdateData(TRUE);
		}
		break;
	case CIRCLEMODE:
		if (m_color == COLOR_BLACK)
		{
			ht.SelectStockObject(BLACK_BRUSH);
		}
		else if (m_color == COLOR_BLUE)
		{
			ht.SelectObject(&blueBr);
		}
		else if (m_color == COLOR_RED)
		{
			ht.SelectObject(&redBr);
		}
		else if (m_color == COLOR_GREEN)
		{
			ht.SelectObject(&greenBr);
		}
		if (!m_ist) {
			m_bO = m_bR = point;
			m_ist++;
		}
		else {
			m_bR = point;
			m_ist--;
			drawCircle(&ht, m_bO, m_bR);
			UpdateData(TRUE);
			ReleaseCapture();
		}
		break;

	case RECTMODE:
		if (m_color == COLOR_BLACK)
		{
			ht.SelectStockObject(BLACK_BRUSH);
		}
		else if (m_color == COLOR_BLUE)
		{
			ht.SelectObject(&blueBr);
		}
		else if (m_color == COLOR_RED)
		{
			ht.SelectObject(&redBr);
		}
		else if (m_color == COLOR_GREEN)
		{
			ht.SelectObject(&greenBr);
		}
		if (!mR_ist) {
			m_rO = m_rR = point;
			mR_ist++;
		}
		else {
			m_rR = point;
			mR_ist--;
			drawRect(&ht, m_rO, m_rR);
			UpdateData(TRUE);
			ReleaseCapture();
		}
		break;

	case POLYGONMODE:
	{
		ASSERT(m_iPolyDotNumbers < 999);
		if (PushNumb == 0) {
			m_ptPolyDotArrays[m_iPolyDotNumbers] = point;
			++m_iPolyDotNumbers;
			PushNumb++;
			mPointOrign = point;
			mPointOld = point;
			UpdateData(TRUE);
			SetCapture();
		}
		else {
			m_ptPolyDotArrays[m_iPolyDotNumbers] = point;
			++m_iPolyDotNumbers;
			ht.MoveTo(mPointOrign);
			ht.LineTo(point);
			mPointOrign = point;
			mPointOld = point;
			UpdateData(TRUE);
		}
		break;
	}

	case ERASEMODE:
		if (!mR_ist) {
			m_rO = m_rR = point;
			mR_ist++;
		}
		else {
			m_rR = point;
			mR_ist--;
			//ht.Rectangle(m_rO.x, m_rO.y, m_rR.x, m_rR.y);
			CRect rect(m_rO, m_rR);
			InvalidateRect(rect);
			UpdateData(TRUE);
			ReleaseCapture();
		}
		break;

	case CURVEMODE:
		if (!curveFlag) {
			mPointOrign = mPointOld = point;
			curveFlag = TRUE;
			SetCapture();
		}
		else {
			mPointOrign = mPointOld = point;
			curveFlag = FALSE;
			ReleaseCapture();
		}
	default:
		break;
	}
	ht.SelectObject(pOldPen);
	CView::OnLButtonDown(nFlags, point);
}



void CMDrawView::OnMouseMove(UINT nFlags, CPoint point)
{
	// TODO: �ڴ������Ϣ�����������/�����Ĭ��ֵ
	CMDrawDoc *pDoc = GetDocument();
	CClientDC ddd(this);
	CPen cPen;
	cPen.CreatePen(penStyle, penWidth, m_color);
	CPen *pOldPen = ddd.SelectObject(&cPen);
	int nDrawMode = ddd.SetROP2(R2_NOTXORPEN);
	if (m_DrawCurrent == LINEMODE && PushNumb == 1) {
		if (mPointOld != point) {
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(mPointOld);
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(point);
			mPointOld = point;
		}
	}
	if (m_DrawCurrent == PLINEMODE && PushNumb > 0) {
		if (mPointOld != point) {
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(mPointOld);
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(point);
			mPointOld = point;
		}
	}
	if (m_DrawCurrent == CIRCLEMODE && m_ist == 1) {
		ddd.SelectStockObject(NULL_BRUSH);
		CPoint prePnt, curPnt;
		prePnt = m_bR;
		curPnt = point;
		drawCircle(&ddd, m_bO, prePnt);
		drawCircle(&ddd, m_bO, curPnt);
		m_bR = point;
		ddd.SetROP2(nDrawMode);
	}
	if (m_DrawCurrent == RECTMODE && mR_ist == 1) {
		ddd.SelectStockObject(NULL_BRUSH);
		CPoint prePnt, curPnt;
		prePnt = m_rR;
		curPnt = point;
		drawRect(&ddd, m_rO, prePnt);
		drawRect(&ddd, m_rO, curPnt);
		m_rR = point;
		ddd.SetROP2(nDrawMode);
	}
	if (m_DrawCurrent == POLYGONMODE && PushNumb > 0) {
		if (mPointOld != point) {
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(mPointOld);
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(point);
			mPointOld = point;
		}
	}
	if (m_DrawCurrent == ERASEMODE && mR_ist == 1) {
		CPen cPen1;
		cPen1.CreatePen(PS_DOT, 1, RGB(255, 0, 0));
		ddd.SelectObject(&cPen1);
		ddd.SelectStockObject(NULL_BRUSH);
		CPoint prePnt, curPnt;
		prePnt = m_rR;
		curPnt = point;
		//drawRect(&ddd, m_rO, prePnt);
		ddd.Rectangle(m_rO.x, m_rO.y, prePnt.x, prePnt.y);
		//drawRect(&ddd, m_rO, curPnt);
		ddd.Rectangle(m_rO.x, m_rO.y, curPnt.x, curPnt.y);
		m_rR = point;
		ddd.SetROP2(nDrawMode);
	}
	if (m_DrawCurrent == CURVEMODE && curveFlag) {
		ddd.SetROP2(R2_COPYPEN);
		drawCurve(&ddd, mPointOrign, point);
	}
	ddd.SelectObject(pOldPen);
	CView::OnMouseMove(nFlags, point);
}


void CMDrawView::OnPaint()
{
	CPaintDC dc(this); // device context for painting
					   // TODO: �ڴ˴������Ϣ����������
					   // ��Ϊ��ͼ��Ϣ���� CView::OnPaint()
}
void CMDrawView::drawCircle(CClientDC* ht, CPoint cenp, CPoint ardp)
{
	int radius = computeRadius(cenp, ardp);
	CRect rc(cenp.x - radius, cenp.y - radius, cenp.x + radius, cenp.y + radius);
	ht->Ellipse(rc);
}


int CMDrawView::computeRadius(CPoint cenp, CPoint ardp)
{
	int dx = cenp.x - ardp.x;
	int dy = cenp.y - ardp.y;
	return (int)sqrt(dx*dx + dy*dy);
}
void CMDrawView::testCircle(CDC* pDC, CPoint cenp, CPoint ardp)
{
	int radius = computeRadius(cenp, ardp);
	CRect rc(cenp.x - radius, cenp.y - radius, cenp.x + radius, cenp.y + radius);
	pDC->Ellipse(rc);
}

void CMDrawView::drawRect(CClientDC* ht, CPoint cPoint, CPoint ePoint)
{
	ht->Rectangle(cPoint.x, cPoint.y, ePoint.x, ePoint.y);
}
void CMDrawView::drawCurve(CClientDC* ht, CPoint first, CPoint second)
{
	ht->MoveTo(first);
	ht->LineTo(second);
	mPointOrign = second;
	mPointOld = second;
}


void CMDrawView::OnDrawCustom()
{
	m_DrawCurrent = CURVEMODE;
}

void CMDrawView::OnRButtonDown(UINT nFlags, CPoint point)
{
	// TODO: �ڴ������Ϣ�����������/�����Ĭ��ֵ
	CMDrawDoc *pDoc = GetDocument();
	CClientDC ddd(this);
	CMainFrame* pMain = (CMainFrame*)AfxGetApp()->m_pMainWnd;
	CPen cPen;
	cPen.CreatePen(penStyle, penWidth, m_color);
	CPen *pOldPen = ddd.SelectObject(&cPen);

	ddd.SetROP2(R2_NOTXORPEN);
	if (m_DrawCurrent == LINEMODE && PushNumb == 1) {
		ddd.MoveTo(mPointOrign);
		ddd.LineTo(mPointOld);
		PushNumb = 0;
		ReleaseCapture();
	}
	if (m_DrawCurrent == PLINEMODE && PushNumb > 0) {
		ddd.MoveTo(mPointOrign);
		ddd.LineTo(mPointOld);
		PushNumb = 0;
		ReleaseCapture();
	}
	if (m_DrawCurrent == CIRCLEMODE && m_ist == 1) {
		ddd.SelectStockObject(NULL_BRUSH);
		drawCircle(&ddd, m_bO, m_bR);
		m_ist = 0;
		ReleaseCapture();

	}
	if (m_DrawCurrent == RECTMODE && mR_ist == 1) {
		ddd.SelectStockObject(NULL_BRUSH);
		drawRect(&ddd, m_rO, m_rR);
		mR_ist = 0;
		ReleaseCapture();
	}
	if (m_DrawCurrent == POLYGONMODE) {
		ddd.SelectStockObject(NULL_BRUSH);
		if (m_iPolyDotNumbers > 2)
		{
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(mPointOld);
			ddd.SetROP2(R2_COPYPEN);
			ddd.Polygon(m_ptPolyDotArrays, m_iPolyDotNumbers);
			m_iPolyDotNumbers = 0;
			PushNumb = 0;
		}
		else {
			ddd.MoveTo(mPointOrign);
			ddd.LineTo(mPointOld);
			ddd.Polygon(m_ptPolyDotArrays, m_iPolyDotNumbers);
			m_iPolyDotNumbers = 0;
			PushNumb = 0;
		}
		ReleaseCapture();
	}
	ddd.SelectObject(pOldPen);
	CView::OnRButtonDown(nFlags, point);
}


void CMDrawView::OnEraseAll()
{
	Invalidate();
	CMainFrame* pMain = (CMainFrame*)AfxGetApp()->m_pMainWnd;
	// TODO: �ڴ���������������
}




void CMDrawView::OnEraseCu()
{
	m_DrawCurrent = ERASEMODE;
	PushNumb = 0;
	// TODO: �ڴ���������������
}


BOOL CMDrawView::OnSetCursor(CWnd* pWnd, UINT nHitTest, UINT message)
{
	// TODO: �ڴ������Ϣ�����������/�����Ĭ��ֵ
	SetCursor(LoadCursor(NULL, IDC_CROSS));
	return TRUE;
	return CView::OnSetCursor(pWnd, nHitTest, message);
}


void CMDrawView::OnDrawCu()
{
	m_DrawCurrent = CURVEMODE;
	// TODO: �ڴ���������������
}


void CMDrawView::ChangePenBlue()
{
	m_color = COLOR_BLUE;
}


void CMDrawView::ChangePenBlack()
{
	// TODO: �ڴ���������������
	m_color = COLOR_BLACK;
}


void CMDrawView::ChangePenRed()
{
	// TODO: �ڴ���������������
	m_color = COLOR_RED;
}


void CMDrawView::ChangePenGreen()
{
	// TODO: �ڴ���������������
	m_color = COLOR_GREEN;
}
