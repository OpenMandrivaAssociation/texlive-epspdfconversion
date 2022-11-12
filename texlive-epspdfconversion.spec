Name:		texlive-epspdfconversion
Version:	18703
Release:	1
Summary:	On-the-fly conversion of EPS to PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epspdfconversion
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
