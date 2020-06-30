<?php

require 'vendor/autoload.php';
use Dompdf\Dompdf;

global $dompdf;
$dompdf = new Dompdf();

function file_get_contents_utf8($fn) {
  $content = file_get_contents($fn);
   return mb_convert_encoding($content, 'UTF-8',
       mb_detect_encoding($content, 'UTF-8, ISO-8859-1', true));
}

function generateReport($htmlPath) {
  global $dompdf;
  $fileContent  = file_get_contents_utf8($htmlPath);
  $dompdf->loadHtml($fileContent, 'UTF-8');
  $dompdf->render();

  return $dompdf->output();
}

$htmlPath = "report_base.html.j2";

if (sizeof($argv) >= 2) {
  $htmlPath = $argv[1];
}

$renderedPdf = generateReport($htmlPath);
file_put_contents("./report.pdf", $renderedPdf);

//$dompdf->setPaper('A4', 'landscape');

//Passa para user como download?
//$dompdf->stream();

//Salva no disco



//./ExecSummary.html
//./BPG_OSCE_Sample.html.cleaned.html
// $fileContent = file_get_contents( './summary.html.temp' ) ;
// $dompdf = new Dompdf();
// $dompdf->loadHtml($fileContent);

//$dompdf->setPaper('A4', 'landscape');
//
// $dompdf->render();

//Passa para user como download?
//$dompdf->stream();

//Salva no disco
// $output = $dompdf->output();
// file_put_contents("./report-executive.pdf", $output);

?>
