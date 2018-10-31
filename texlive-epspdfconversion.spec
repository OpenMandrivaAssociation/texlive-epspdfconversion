# revision 18703
# category Package
# catalog-ctan /macros/latex/contrib/epspdfconversion
# catalog-date 2010-06-02 10:36:47 +0200
# catalog-license lppl
# catalog-version 0.61
Name:		texlive-epspdfconversion
Version:	0.61
Release:	11
Summary:	On-the-fly conversion of EPS to PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epspdfconversion
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package calls the epstopdf package to convert EPS graphics
to PDF, on the fly. It servs as a vehicle for passing
conversion options (such as grayscale, prepress or pdfversion)
to the epspdf converter.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/epspdfconversion/epspdfconversion.sty
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/README
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/epspdfconversion.pdf
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/epspdfconversion_docu.tex
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/image.eps
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/image2.eps
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/optionstable.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.61-2
+ Revision: 751534
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.61-1
+ Revision: 718353
- texlive-epspdfconversion
- texlive-epspdfconversion
- texlive-epspdfconversion
- texlive-epspdfconversion

