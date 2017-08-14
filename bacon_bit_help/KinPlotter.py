import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import sys
import Plotting_Header
from Plotting_Header import *

def MakeKinPlots(F, N):
	print " -------------------- Making KinPlots for " + N
	print " -------------------- Creating Histograms"
	outfile = TFile("Histograms/Hists_"+N+".root", "recreate")

#        folder1 = TDirectory()
#        folder1.Add(outfile.mkdir("NoCuts"))

#        folder2 = TDirectory()
#        folder2.Add(outfile.mkdir("ElePfMet"))

#        folder3 = TDirectory()
#        folder3.Add(outfile.mkdir("MuoPfMet"))

#        folder4 = TDirectory()
#        folder4.Add(outfile.mkdir("ElePuppet"))

#        folder5 = TDirectory()
#        folder5.Add(outfile.mkdir("MuoPuppet"))

#No Cuts (defining Histograms)
#        folder1.cd()
	#
	Jet_0 = TH1F(N+"_AK8_Jet_0", "", 200, 0, 1000)
	Jet_0.GetXaxis().SetTitle("Leading AK8 Jet (GeV)")
	Jet_0.GetXaxis().SetTitleSize(0.045)
	Jet_0.GetYaxis().SetTitle("Events")
	Jet_0.GetYaxis().SetTitleSize(0.045)
	#
	Jet_Pt_0 = TH1F(N+"_AK8_Jet_Pt_0", "", 200, 0, 1000)
	Jet_Pt_0.GetXaxis().SetTitle("Leading AK8 Jet (GeV)")
	Jet_Pt_0.GetXaxis().SetTitleSize(0.045)
	Jet_Pt_0.GetYaxis().SetTitle("Events")
	Jet_Pt_0.GetYaxis().SetTitleSize(0.045)
	#
	AK4_Jet_0 = TH1F(N+"_AK4_Jet_0", "", 200, 0, 1000)
	AK4_Jet_0.GetXaxis().SetTitle("AK4_0 Jet (GeV)")
	AK4_Jet_0.GetXaxis().SetTitleSize(0.045)
	AK4_Jet_0.GetYaxis().SetTitle("Events")
	AK4_Jet_0.GetYaxis().SetTitleSize(0.045)
	#
	AK4_Jet_1 = TH1F(N+"_AK4_Jet_1", "", 200, 0, 1000)
	AK4_Jet_1.GetXaxis().SetTitle("AK4_1 Jet (GeV)")
	AK4_Jet_1.GetXaxis().SetTitleSize(0.045)
	AK4_Jet_1.GetYaxis().SetTitle("Events")
	AK4_Jet_1.GetYaxis().SetTitleSize(0.045)
	#
	AK4_Jet_2 = TH1F(N+"_AK4_Jet_2", "", 200, 0, 1000)
	AK4_Jet_2.GetXaxis().SetTitle("AK4_2 Jet (GeV)")
	AK4_Jet_2.GetXaxis().SetTitleSize(0.045)
	AK4_Jet_2.GetYaxis().SetTitle("Events")
	AK4_Jet_2.GetYaxis().SetTitleSize(0.045)
	#
	AK4_Jet_3 = TH1F(N+"_AK4_Jet_3", "", 200, 0, 1000)
	AK4_Jet_3.GetXaxis().SetTitle("AK4_3 Jet (GeV)")
	AK4_Jet_3.GetXaxis().SetTitleSize(0.045)
	AK4_Jet_3.GetYaxis().SetTitle("Events")
	AK4_Jet_3.GetYaxis().SetTitleSize(0.045)
	#
	AK4_Jet_Pt_0 = TH1F(N+"_Jet_Pt_0", "", 200, 0, 1000)
	AK4_Jet_Pt_0.GetXaxis().SetTitle("Leading AK8 Jet p_{T} (GeV)")
	AK4_Jet_Pt_0.GetXaxis().SetTitleSize(0.045)
	AK4_Jet_Pt_0.GetYaxis().SetTitle("Events")
	AK4_Jet_Pt_0.GetYaxis().SetTitleSize(0.045)
	#
	Jet_Mass_0 = TH1F(N+"_Jet_Mass_0", "", 80, 0, 400)
        Jet_Mass_0.GetXaxis().SetTitle("Leading AK8 Jet Mass (GeV)")
        Jet_Mass_0.GetXaxis().SetTitleSize(0.045)
        Jet_Mass_0.GetYaxis().SetTitle("Events")
        Jet_Mass_0.GetYaxis().SetTitleSize(0.045)
	#
	Jet_Phi_0 = TH1F(N+"_Jet_Phi_0", "", 100, -3.7, 3.7)
        Jet_Phi_0.GetXaxis().SetTitle("Leading AK8 Jet #phi")
        Jet_Phi_0.GetXaxis().SetTitleSize(0.045)
        Jet_Phi_0.GetYaxis().SetTitle("Events")
        Jet_Phi_0.GetYaxis().SetTitleSize(0.045)
        #       
	Jet_Eta_0 = TH1F(N+"_Jet_Eta_0", "", 60, -3, 3)
        Jet_Eta_0.GetXaxis().SetTitle("Leading Jet #eta")
        Jet_Eta_0.GetXaxis().SetTitleSize(0.045)
        Jet_Eta_0.GetYaxis().SetTitle("Events")
        Jet_Eta_0.GetYaxis().SetTitleSize(0.045)
	#
	NJets = TH1F(N + "_NJets", "", 6, 0, 6)
	NJets.GetXaxis().SetTitle("Number of Jets")
	NJets.GetXaxis().SetTitleSize(0.045)
        NJets.GetYaxis().SetTitle("Events")
        NJets.GetYaxis().SetTitleSize(0.045)
	#
	Npv = TH1F(N+"_Npv", "", 180, 0, 90)
        Npv.GetXaxis().SetTitle("Number of Primary Vertices")
        Npv.GetXaxis().SetTitleSize(0.045)
        Npv.GetYaxis().SetTitle("Events")
        Npv.GetYaxis().SetTitleSize(0.045)
	#
	PfMet = TH1F(N+"_PfMet", "", 200, 0, 1000)
        PfMet.GetXaxis().SetTitle("pf MET")
        PfMet.GetXaxis().SetTitleSize(0.045)
        PfMet.GetYaxis().SetTitle("Events")
        PfMet.GetYaxis().SetTitleSize(0.045)
	#
	PuppiMet = TH1F(N+"_PuppiMet", "", 200, 0, 1000)
        PuppiMet.GetXaxis().SetTitle("Puppi MET")
        PuppiMet.GetXaxis().SetTitleSize(0.045)
        PuppiMet.GetYaxis().SetTitle("Events")
        PuppiMet.GetYaxis().SetTitleSize(0.045)
	#
	PfMet_phi = TH1F(N+"_PfMet_phi", "", 100, -3.7, 3.7)
	PfMet_phi.GetXaxis().SetTitle("PfMet phi")
	PfMet_phi.GetXaxis().SetTitleSize(0.045)
	PfMet_phi.GetYaxis().SetTitle("Events")
	PfMet_phi.GetYaxis().SetTitleSize(0.045)
	#
	PuppiMet_phi = TH1F(N+"_PuppiMet_phi", "", 100, -3.7, 3.7)
	PuppiMet_phi.GetXaxis().SetTitle("PuppiMet phi")
	PuppiMet_phi.GetXaxis().SetTitleSize(0.045)
	PuppiMet_phi.GetYaxis().SetTitle("Events")
	PuppiMet_phi.GetYaxis().SetTitleSize(0.045)
	#
	Muo_0_pt = TH1F(N+"_muo_pt", "", 200, 0, 1000)
	Muo_0_pt.GetXaxis().SetTitle("muo pt")
	Muo_0_pt.GetXaxis().SetTitleSize(0.045)
	Muo_0_pt.GetYaxis().SetTitle("Events")
	Muo_0_pt.GetYaxis().SetTitleSize(0.045)
	#
	Muo_0_eta = TH1F(N+"_muo_eta", "", 60, -3, 3)
	Muo_0_eta.GetXaxis().SetTitle("muo eta")
	Muo_0_eta.GetXaxis().SetTitleSize(0.045)
	Muo_0_eta.GetYaxis().SetTitle("Events")
	Muo_0_eta.GetYaxis().SetTitleSize(0.045)
	#
	Muo_0_phi = TH1F(N+"_muo_phi", "", 100, -3.7, 3.7)
	Muo_0_phi.GetXaxis().SetTitle("muo phi")
	Muo_0_phi.GetXaxis().SetTitleSize(0.045)
	Muo_0_phi.GetYaxis().SetTitle("Events")
	Muo_0_phi.GetYaxis().SetTitleSize(0.045)	
	#
	Ele_0_pt = TH1F(N+"_ele_pt", "", 200, 0, 1000)
	Ele_0_pt.GetXaxis().SetTitle("ele pt")
	Ele_0_pt.GetXaxis().SetTitleSize(0.045)
	Ele_0_pt.GetYaxis().SetTitle("Events")
	Ele_0_pt.GetYaxis().SetTitleSize(0.045)	
	#
	Ele_0_eta = TH1F(N+"_ele_eta", "", 60, -3, 3)
	Ele_0_eta.GetXaxis().SetTitle("ele eta")
	Ele_0_eta.GetXaxis().SetTitleSize(0.045)
	Ele_0_eta.GetYaxis().SetTitle("Events")
	Ele_0_eta.GetYaxis().SetTitleSize(0.045)	
	#
	Ele_0_phi = TH1F(N+"_ele_phi", "", 100, -3.7, 3.7)
	Ele_0_phi.GetXaxis().SetTitle("ele phi")
	Ele_0_phi.GetXaxis().SetTitleSize(0.045)
	Ele_0_phi.GetYaxis().SetTitle("Events")
	Ele_0_phi.GetYaxis().SetTitleSize(0.045)	
	#
	Mt_Muo_Puppi = TH1F(N+"_Mt_Muo_Puppi", "", 500, 0, 1000)
	Mt_Muo_Puppi.GetXaxis().SetTitle("Muo Mt using PuppiMet")
	Mt_Muo_Puppi.GetXaxis().SetTitleSize(0.045)
	Mt_Muo_Puppi.GetYaxis().SetTitle("Events")
	Mt_Muo_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Mt_Ele_Puppi = TH1F(N+"_Mt_Ele_Puppi", "", 500, 0, 1000)
	Mt_Ele_Puppi.GetXaxis().SetTitle("Ele Mt using PuppiMet")
	Mt_Ele_Puppi.GetXaxis().SetTitleSize(0.045)
	Mt_Ele_Puppi.GetYaxis().SetTitle("Events")
	Mt_Ele_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Mt_Muo_Pf = TH1F(N+"_Mt_Muo_Pf", "", 500, 0, 1000)
	Mt_Muo_Pf.GetXaxis().SetTitle("Muo Mt using PfMet")
	Mt_Muo_Pf.GetXaxis().SetTitleSize(0.045)
	Mt_Muo_Pf.GetYaxis().SetTitle("Events")
	Mt_Muo_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Mt_Ele_Pf = TH1F(N+"_Mt_Ele_Pf", "", 500, 0, 1000)
	Mt_Ele_Pf.GetXaxis().SetTitle("Ele Mt using PfMet")
	Mt_Ele_Pf.GetXaxis().SetTitleSize(0.045)
	Mt_Ele_Pf.GetYaxis().SetTitle("Events")
	Mt_Ele_Pf.GetYaxis().SetTitleSize(0.045)
	#
	weight_one = TH1F(N + "_weight-1", "", 50, 0, 5)
	weight_one.GetXaxis().SetTitle("weight one")
	weight_one.GetXaxis().SetTitleSize(0.045)
	weight_one.GetYaxis().SetTitle("Events")
	weight_one.GetYaxis().SetTitleSize(0.045)
	#
	weight_no_k = TH1F(N + "_weight_no_k", "", 50, 0, 5)
	weight_no_k.GetXaxis().SetTitle("puWeight * scale1fb")
	weight_no_k.GetXaxis().SetTitleSize(0.045)
	weight_no_k.GetYaxis().SetTitle("Events")
	weight_no_k.GetYaxis().SetTitleSize(0.045)
	#
	weight_k = TH1F(N + "_weight_k", "", 50, 0, 5)
	weight_k.GetXaxis().SetTitle("kfactor * kfactorNLO")
	weight_k.GetXaxis().SetTitleSize(0.045)
	weight_k.GetYaxis().SetTitle("Events")
	weight_k.GetYaxis().SetTitleSize(0.045)
	#
	weight_original = TH1F(N + "_weight-original", "", 50, 0, 5)
	weight_original.GetXaxis().SetTitle("puWeight * scale1fb * kfactor * kfactorNLO")
	weight_original.GetXaxis().SetTitleSize(0.045)
	weight_original.GetYaxis().SetTitle("Events")
	weight_original.GetYaxis().SetTitleSize(0.045)
	#
	weight_new = TH1F(N + "_weight_new", "" , 50, 0, 5)
	weight_new.GetXaxis().SetTitle("evtWeight")
	weight_new.GetXaxis().SetTitleSize(0.045)
	weight_new.GetYaxis().SetTitle("Events")
	weight_new.GetYaxis().SetTitleSize(0.045)
	#
	weight_pu = TH1F(N + "_weight_pu", "", 50, 0, 5)
	weight_pu.GetXaxis().SetTitle("puWeight")
	weight_pu.GetXaxis().SetTitleSize(0.045)
	weight_pu.GetYaxis().SetTitle("Events")
	weight_pu.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_ele_AK4_0 = TH1F(N + "_delta_R_ele_AK4_0", "", 50, 0, 2*TMath.Pi())
	delta_R_ele_AK4_0.GetXaxis().SetTitle("delta R for electron and AK4_0")
	delta_R_ele_AK4_0.GetXaxis().SetTitleSize(0.045)
	delta_R_ele_AK4_0.GetYaxis().SetTitle("Events")
	delta_R_ele_AK4_0.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_ele_AK4_1 = TH1F(N + "_delta_R_ele_AK4_1", "", 50, 0, 2*TMath.Pi())
	delta_R_ele_AK4_1.GetXaxis().SetTitle("delta R for electron and AK4_1")
	delta_R_ele_AK4_1.GetXaxis().SetTitleSize(0.045)
	delta_R_ele_AK4_1.GetYaxis().SetTitle("Events")
	delta_R_ele_AK4_1.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_ele_AK4_2 = TH1F(N + "_delta_R_ele_AK4_2", "", 50, 0, 2*TMath.Pi())
	delta_R_ele_AK4_2.GetXaxis().SetTitle("delta R for electron and AK4_2")
	delta_R_ele_AK4_2.GetXaxis().SetTitleSize(0.045)
	delta_R_ele_AK4_2.GetYaxis().SetTitle("Events")
	delta_R_ele_AK4_2.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_ele_AK4_3 = TH1F(N + "_delta_R_ele_AK4_3", "", 50, 0, 2*TMath.Pi())
	delta_R_ele_AK4_3.GetXaxis().SetTitle("delta R for electron and AK4_3")
	delta_R_ele_AK4_3.GetXaxis().SetTitleSize(0.045)
	delta_R_ele_AK4_3.GetYaxis().SetTitle("Events")
	delta_R_ele_AK4_3.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_muo_AK4_0 = TH1F(N + "_delta_R_muo_AK4_0", "", 50, 0, 2*TMath.Pi())
	delta_R_muo_AK4_0.GetXaxis().SetTitle("delta R for muon and AK4_0")
	delta_R_muo_AK4_0.GetXaxis().SetTitleSize(0.045)
	delta_R_muo_AK4_0.GetYaxis().SetTitle("Events")
	delta_R_muo_AK4_0.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_muo_AK4_1 = TH1F(N + "_delta_R_muo_AK4_1", "", 50, 0, 2*TMath.Pi())
	delta_R_muo_AK4_1.GetXaxis().SetTitle("delta R for muon and AK4_1")
	delta_R_muo_AK4_1.GetXaxis().SetTitleSize(0.045)
	delta_R_muo_AK4_1.GetYaxis().SetTitle("Events")
	delta_R_muo_AK4_1.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_muo_AK4_2 = TH1F(N + "_delta_R_muo_AK4_2", "", 50, 0, 2*TMath.Pi())
	delta_R_muo_AK4_2.GetXaxis().SetTitle("delta R for muon and AK4_2")
	delta_R_muo_AK4_2.GetXaxis().SetTitleSize(0.045)
	delta_R_muo_AK4_2.GetYaxis().SetTitle("Events")
	delta_R_muo_AK4_2.GetYaxis().SetTitleSize(0.045)
	#
	delta_R_muo_AK4_3 = TH1F(N + "_delta_R_muo_AK4_3", "", 50, 0, 2*TMath.Pi())
	delta_R_muo_AK4_3.GetXaxis().SetTitle("delta R for muon and AK4_3")
	delta_R_muo_AK4_3.GetXaxis().SetTitleSize(0.045)
	delta_R_muo_AK4_3.GetYaxis().SetTitle("Events")
	delta_R_muo_AK4_3.GetYaxis().SetTitleSize(0.045)
	#
	Low_angle_elePt_over_pfmet = TH1F(N + "_low_angle_elePt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	Low_angle_elePt_over_pfmet.GetXaxis().SetTitle("Angle between ElePt and PfMet")
	Low_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Low_angle_elePt_over_pfmet.GetYaxis().SetTitle("Events")
	Low_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Low_angle_muoPt_over_pfmet = TH1F(N + "_low_angle_muoPt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	Low_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Angle between MuoPt and PfMet")
	Low_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Low_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Events")
	Low_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#				    
	Low_angle_elePt_over_puppet = TH1F(N + "_low_angle_elePt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	Low_angle_elePt_over_puppet.GetXaxis().SetTitle("Angle between ElePt and Puppi Met")
	Low_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Low_angle_elePt_over_puppet.GetYaxis().SetTitle("Events")
	Low_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Low_angle_muoPt_over_puppet = TH1F(N + "_lowangle_muoPt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	Low_angle_muoPt_over_puppet.GetXaxis().SetTitle("Angle between MuoPt and Puppi Met")
	Low_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Low_angle_muoPt_over_puppet.GetYaxis().SetTitle("Events")
	Low_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	High_angle_elePt_over_pfmet = TH1F(N + "_high_angle_elePt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	High_angle_elePt_over_pfmet.GetXaxis().SetTitle("Angle between ElePt and PfMet")
	High_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	High_angle_elePt_over_pfmet.GetYaxis().SetTitle("Events")
	High_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	High_angle_muoPt_over_pfmet = TH1F(N + "_high_angle_muoPt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	High_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Angle between MuoPt and PfMet")
	High_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	High_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Events")
	High_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#				    
	High_angle_elePt_over_puppet = TH1F(N + "_high_angle_elePt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	High_angle_elePt_over_puppet.GetXaxis().SetTitle("Angle between ElePt and Puppi Met")
	High_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	High_angle_elePt_over_puppet.GetYaxis().SetTitle("Events")
	High_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	High_angle_muoPt_over_puppet = TH1F(N + "_high_angle_muoPt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	High_angle_muoPt_over_puppet.GetXaxis().SetTitle("Angle between MuoPt and Puppi Met")
	High_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	High_angle_muoPt_over_puppet.GetYaxis().SetTitle("Events")
	High_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	JetPt_vs_elePt = TH2F(N+"_JetPt_vs_elePt", "", 200, 0, 1000, 200, 0, 1000)
	JetPt_vs_elePt.GetXaxis().SetTitle("ele Pt")
	JetPt_vs_elePt.GetXaxis().SetTitleSize(0.045)
	JetPt_vs_elePt.GetYaxis().SetTitle("Jet Pt")
	JetPt_vs_elePt.GetYaxis().SetTitleSize(0.045)
	#
	JetPt_vs_muoPt = TH2F(N+"_JetPt_vs_muoPt", "", 200, 0, 1000, 200, 0, 1000)
	JetPt_vs_muoPt.GetXaxis().SetTitle("muo Pt")
	JetPt_vs_muoPt.GetXaxis().SetTitleSize(0.045)
	JetPt_vs_muoPt.GetYaxis().SetTitle("Jet Pt")
	JetPt_vs_muoPt.GetYaxis().SetTitleSize(0.045)
	#
	elePt_vs_PfMET = TH2F(N+"_elePt_vs_PfMET", "", 200, 0, 1000, 200, 0, 1000)
	elePt_vs_PfMET.GetXaxis().SetTitle("PfMET")
	elePt_vs_PfMET.GetXaxis().SetTitleSize(0.045)
	elePt_vs_PfMET.GetYaxis().SetTitle("ele Pt")
	elePt_vs_PfMET.GetYaxis().SetTitleSize(0.045)
	#
	muoPt_vs_PfMET = TH2F(N+"_muoPt_vs_PfMET", "", 200, 0, 1000, 200, 0, 1000)
	muoPt_vs_PfMET.GetXaxis().SetTitle("PfMET")
	muoPt_vs_PfMET.GetXaxis().SetTitleSize(0.045)
	muoPt_vs_PfMET.GetYaxis().SetTitle("muo Pt")
	muoPt_vs_PfMET.GetYaxis().SetTitleSize(0.045)
	#
	elePt_vs_PuppiMET = TH2F(N+"_elePt_vs_PuppiMET", "", 200, 0, 1000, 200, 0, 1000)
	elePt_vs_PuppiMET.GetXaxis().SetTitle("PuppiMET")
	elePt_vs_PuppiMET.GetXaxis().SetTitleSize(0.045)
	elePt_vs_PuppiMET.GetYaxis().SetTitle("ele Pt using")
	elePt_vs_PuppiMET.GetYaxis().SetTitleSize(0.045)
	#
	muoPt_vs_PuppiMET = TH2F(N+"_muoPt_vs_PuppiMET", "", 200, 0, 1000, 200, 0, 1000)
	muoPt_vs_PuppiMET.GetXaxis().SetTitle("PuppiMET")
	muoPt_vs_PuppiMET.GetXaxis().SetTitleSize(0.045)
	muoPt_vs_PuppiMET.GetYaxis().SetTitle("muo Pt")
	muoPt_vs_PuppiMET.GetYaxis().SetTitleSize(0.045)
	#
	eleMt_vs_JetPt_Pf = TH2F(N+"_eleMt_vs_JetPt_Pf", "", 500, 0, 1000, 100, 0, 1000)
	eleMt_vs_JetPt_Pf.GetXaxis().SetTitle("Jet Pt")
	eleMt_vs_JetPt_Pf.GetXaxis().SetTitleSize(0.045)
	eleMt_vs_JetPt_Pf.GetYaxis().SetTitle("ele Mt using PfMet")
	eleMt_vs_JetPt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	muoMt_vs_JetPt_Pf = TH2F(N+"_muoMt_vs_JetPt_Pf", "", 500, 0, 1000, 100, 0, 1000)
	muoMt_vs_JetPt_Pf.GetXaxis().SetTitle("Jet Pt")
	muoMt_vs_JetPt_Pf.GetXaxis().SetTitleSize(0.045)
	muoMt_vs_JetPt_Pf.GetYaxis().SetTitle("muo Mt using PfMet")
	muoMt_vs_JetPt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	eleMt_vs_JetPt_Puppi = TH2F(N+"_eleMt_vs_JetPt_Puppi", "", 500, 0, 1000, 100, 0, 1000)
	eleMt_vs_JetPt_Puppi.GetXaxis().SetTitle("Jet_Pt")
	eleMt_vs_JetPt_Puppi.GetXaxis().SetTitleSize(0.045)
	eleMt_vs_JetPt_Puppi.GetYaxis().SetTitle("ele Mt using PuppiMet")
	eleMt_vs_JetPt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	muoMt_vs_JetPt_Puppi = TH2F(N+"_muoMt_vs_JetPt_Puppi", "", 500, 0, 1000, 100, 0, 1000)
	muoMt_vs_JetPt_Puppi.GetXaxis().SetTitle("Jet_Pt")
	muoMt_vs_JetPt_Puppi.GetXaxis().SetTitleSize(0.045)
	muoMt_vs_JetPt_Puppi.GetYaxis().SetTitle("muo Mt using PuppiMet")
	muoMt_vs_JetPt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	JetPhi_vs_elePhi = TH2F(N+"_JetPhi_vs_elePhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	JetPhi_vs_elePhi.GetXaxis().SetTitle("ele phi")
	JetPhi_vs_elePhi.GetXaxis().SetTitleSize(0.045)
	JetPhi_vs_elePhi.GetYaxis().SetTitle("Jet phi")
	JetPhi_vs_elePhi.GetYaxis().SetTitleSize(0.045)
	#
	JetPhi_vs_muoPhi = TH2F(N+"_JetPhi_vs_muoPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	JetPhi_vs_muoPhi.GetXaxis().SetTitle("muo phi")
	JetPhi_vs_muoPhi.GetXaxis().SetTitleSize(0.045)
	JetPhi_vs_muoPhi.GetYaxis().SetTitle("Jet phi")
	JetPhi_vs_muoPhi.GetYaxis().SetTitleSize(0.045)
	#
	elePhi_vs_PfMETPhi = TH2F(N+"_elePhi_vs_PfMETPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	elePhi_vs_PfMETPhi.GetXaxis().SetTitle("PfMET phi")
	elePhi_vs_PfMETPhi.GetXaxis().SetTitleSize(0.045)
	elePhi_vs_PfMETPhi.GetYaxis().SetTitle("ele phi")
	elePhi_vs_PfMETPhi.GetYaxis().SetTitleSize(0.045)
	#
	muoPhi_vs_PfMETPhi = TH2F(N+"_muoPhi_vs_PfMETPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	muoPhi_vs_PfMETPhi.GetXaxis().SetTitle("PfMET phi")
	muoPhi_vs_PfMETPhi.GetXaxis().SetTitleSize(0.045)
	muoPhi_vs_PfMETPhi.GetYaxis().SetTitle("muo phi")
	muoPhi_vs_PfMETPhi.GetYaxis().SetTitleSize(0.045)
	#
	elePhi_vs_PuppiMETPhi = TH2F(N+"_elePhi_vs_PuppiMETPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	elePhi_vs_PuppiMETPhi.GetXaxis().SetTitle("PuppiMET_phi")
	elePhi_vs_PuppiMETPhi.GetXaxis().SetTitleSize(0.045)
	elePhi_vs_PuppiMETPhi.GetYaxis().SetTitle("ele phi")
	elePhi_vs_PuppiMETPhi.GetYaxis().SetTitleSize(0.045)
	#
	muoPhi_vs_PuppiMETPhi = TH2F(N+"_muoPhi_vs_PuppiMETPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	muoPhi_vs_PuppiMETPhi.GetXaxis().SetTitle("PuppiMET phi")
	muoPhi_vs_PuppiMETPhi.GetXaxis().SetTitleSize(0.045)
	muoPhi_vs_PuppiMETPhi.GetYaxis().SetTitle("muo phi")
	muoPhi_vs_PuppiMETPhi.GetYaxis().SetTitleSize(0.045)
	#
	JetPhi_vs_PfMETPhi = TH2F(N+"_JetPhi_vs_PfMETPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	JetPhi_vs_PfMETPhi.GetXaxis().SetTitle("PfMET phi")
	JetPhi_vs_PfMETPhi.GetXaxis().SetTitleSize(0.045)
	JetPhi_vs_PfMETPhi.GetYaxis().SetTitle("Jet phi")
	JetPhi_vs_PfMETPhi.GetYaxis().SetTitleSize(0.045)
	#
	JetPhi_vs_PuppiMETPhi = TH2F(N+"_JetPhi_vs_PuupiMETPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	JetPhi_vs_PuppiMETPhi.GetXaxis().SetTitle("PuupiMET phi")
	JetPhi_vs_PuppiMETPhi.GetXaxis().SetTitleSize(0.045)
	JetPhi_vs_PuppiMETPhi.GetYaxis().SetTitle("Jet phi")
	JetPhi_vs_PuppiMETPhi.GetYaxis().SetTitleSize(0.045)
	#
#	deltaR_AK41_vs_atan_angle_pfmet_over_elePt = TH2F(N+"_atan_pfmet_over_elePt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetXaxis().SetTitle("Delta R of AK4_1") 
#	deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetXaxis().SetTitleSize(0.045)
#	deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetYaxis().SetTitle("Angle of pi/4 - atan(pfmet/elePt)")
#	deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetYaxis().SetTitleSize(0.045)
	#
#	deltaR_AK41_vs_atan_angle_pfmet_over_muoPt = TH2F(N+"_atan_pfmet_over_muoPt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetXaxis().SetTitle("Delta R of AK4_1") 
#	deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetXaxis().SetTitleSize(0.045)
#	deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetYaxis().SetTitle("Angle of pi/4 - atan(pfmet/muoPt)")
#	deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetYaxis().SetTitleSize(0.045)
	#
#	deltaR_AK41_vs_atan_angle_puppet_over_elePt = TH2F(N+"_atan_puppet_over_elePt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetXaxis().SetTitle("Delta R of AK4_1") 
#	deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetXaxis().SetTitleSize(0.045)
#	deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetYaxis().SetTitle("Angle of pi/4 - atan(puppet/elePt)")
#	deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetYaxis().SetTitleSize(0.045)
	#
#	deltaR_AK41_vs_atan_angle_puppet_over_muoPt = TH2F(N+"_atan_puppet_over_muoPt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetXaxis().SetTitle("Delta R of AK4_1") 
#	deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetXaxis().SetTitleSize(0.045)
#	deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetYaxis().SetTitle("Angle of pi/4 - atan(pfmet/elePt)")
#	deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetYaxis().SetTitleSize(0.045)
	#

#Electron Cuts with Pf MET (defining Histograms)
#       folder2.cd()
	#
	Cut_Jet_Mass_e_Pf_0 = TH1F(N+"_Cut_Jet_Mass_e_Pf_0", "", 80, 0, 400)
        Cut_Jet_Mass_e_Pf_0.GetXaxis().SetTitle("Leading AK8 Jet Mass ele cuts using PfMet(GeV)")
        Cut_Jet_Mass_e_Pf_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Mass_e_Pf_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Mass_e_Pf_0.GetYaxis().SetTitleSize(0.045)
	#
        Cut_Jet_Phi_e_Pf_0 = TH1F(N+"_Cut_Jet_Phi_e_Pf_0", "", 100, -3.7, 3.7)
        Cut_Jet_Phi_e_Pf_0.GetXaxis().SetTitle("Leading AK8 Jet #phi ele cuts using PfMet")
        Cut_Jet_Phi_e_Pf_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Phi_e_Pf_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Phi_e_Pf_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Jet_Eta_e_Pf_0 = TH1F(N+"_Cut_Jet_Eta_e_Pf_0", "", 60, -3, 3)
        Cut_Jet_Eta_e_Pf_0.GetXaxis().SetTitle("Leading Jet #eta ele cuts using PfMet")
        Cut_Jet_Eta_e_Pf_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Eta_e_Pf_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Eta_e_Pf_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_NJets_e_Pf = TH1F(N + "_Cut_NJets_Pf_e", "", 6, 0, 6)
        Cut_NJets_e_Pf.GetXaxis().SetTitle("Number of Jets ele cuts using PfMet")
        Cut_NJets_e_Pf.GetXaxis().SetTitleSize(0.045)
        Cut_NJets_e_Pf.GetYaxis().SetTitle("Events")
        Cut_NJets_e_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Npv_e_Pf = TH1F(N+"_Cut_Npv_e_Pf", "", 180, 0, 90) 
        Cut_Npv_e_Pf.GetXaxis().SetTitle("Number of Primary Vertices ele cuts using PfMet")
        Cut_Npv_e_Pf.GetXaxis().SetTitleSize(0.045)
        Cut_Npv_e_Pf.GetYaxis().SetTitle("Events")
        Cut_Npv_e_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PfMet_Phi_e = TH1F(N+"_Cut_PfMet_phi_e", "", 100, -3.7, 3.7)
	Cut_PfMet_Phi_e.GetXaxis().SetTitle("PfMet phi ele cuts")
	Cut_PfMet_Phi_e.GetXaxis().SetTitleSize(0.045)
	Cut_PfMet_Phi_e.GetYaxis().SetTitle("Events")
	Cut_PfMet_Phi_e.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PfMet_e = TH1F(N+"_Cut_PFMET_e", "", 200, 0, 1000)
        Cut_PfMet_e.GetXaxis().SetTitle("pf MET ele cuts")
        Cut_PfMet_e.GetXaxis().SetTitleSize(0.045)
        Cut_PfMet_e.GetYaxis().SetTitle("Events")
        Cut_PfMet_e.GetYaxis().SetTitleSize(0.045)
	#
	Cut_ele_pt_Pf = TH1F(N+"_Cut_ele_pt_Pf", "", 200, 0, 1000)
	Cut_ele_pt_Pf.GetXaxis().SetTitle("Cut ele pt using PfMet")
	Cut_ele_pt_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_ele_pt_Pf.GetYaxis().SetTitle("Events")
	Cut_ele_pt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_ele_phi_Pf = TH1F(N+"_Cut_ele_phi_Pf", "", 100, -3.7, 3.7)
	Cut_ele_phi_Pf.GetXaxis().SetTitle("Cut ele phi using PfMet")
	Cut_ele_phi_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_ele_phi_Pf.GetYaxis().SetTitle("Events")
	Cut_ele_phi_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_ele_eta_Pf = TH1F(N+"_Cut_ele_eta_Pf", "", 60, -3, 3)
	Cut_ele_eta_Pf.GetXaxis().SetTitle("Cut ele eta using PfMet")
	Cut_ele_eta_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_ele_eta_Pf.GetYaxis().SetTitle("Events")
	Cut_ele_eta_Pf.GetYaxis().SetTitleSize(0.045)	
	#
	Cut_Mt_Ele_Pf = TH1F(N+"_Cut_Mt_Ele_Pf", "", 500, 0, 1000)
	Cut_Mt_Ele_Pf.GetXaxis().SetTitle("Cut Mt Ele using PfMet")
	Cut_Mt_Ele_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_Mt_Ele_Pf.GetYaxis().SetTitle("Events")
	Cut_Mt_Ele_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_0_pf = TH1F(N + "_delta_R_ele_AK4_0_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_0_pf.GetXaxis().SetTitle("delta R for electron and AK4_0 with pfmet cuts")
	Cut_delta_R_ele_AK4_0_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_0_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_0_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_1_pf = TH1F(N + "_Cut_delta_R_ele_AK4_1_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_1_pf.GetXaxis().SetTitle("delta R for electron and AK4_1 with pfmet cuts")
	Cut_delta_R_ele_AK4_1_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_1_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_1_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_2_pf = TH1F(N + "_Cut_delta_R_ele_AK4_2_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_2_pf.GetXaxis().SetTitle("delta R for electron and AK4_2 with pfmet cuts")
	Cut_delta_R_ele_AK4_2_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_2_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_2_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_3_pf = TH1F(N + "_Cut_delta_R_ele_AK4_3_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_3_pf.GetXaxis().SetTitle("delta R for electron and AK4_3 with pfmet cuts")
	Cut_delta_R_ele_AK4_3_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_3_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_3_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Low_angle_elePt_over_pfmet = TH1F(N + "_Cut_low_angle_elePt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_Low_angle_elePt_over_pfmet.GetXaxis().SetTitle("Cut Angle between ElePt and PfMet")
	Cut_Low_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_Low_angle_elePt_over_pfmet.GetYaxis().SetTitle("Events")
	Cut_Low_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_High_angle_elePt_over_pfmet = TH1F(N + "_Cut_high_angle_elePt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_High_angle_elePt_over_pfmet.GetXaxis().SetTitle("Cut Angle from midline between ElePt and PfMet")
	Cut_High_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_High_angle_elePt_over_pfmet.GetYaxis().SetTitle("Events")
	Cut_High_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPt_vs_CutelePt_Pf = TH2F(N+"_CutJetPt_vs_CutelePt_Pf", "", 200, 0, 1000, 200, 0, 1000)
	CutJetPt_vs_CutelePt_Pf.GetXaxis().SetTitle("Cut ele Pt using PfMet")
	CutJetPt_vs_CutelePt_Pf.GetXaxis().SetTitleSize(0.045)
	CutJetPt_vs_CutelePt_Pf.GetYaxis().SetTitle("Cut Jet Pt with ele cuts using PfMet")
	CutJetPt_vs_CutelePt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPfMET_WEIGHT_ONE = TH2F(N+"_CutelePt_vs_CutPfMET_weight_one", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPfMET_WEIGHT_ONE.GetXaxis().SetTitle("Cut PfMET using weight=1")
	CutelePt_vs_CutPfMET_WEIGHT_ONE.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPfMET_WEIGHT_ONE.GetYaxis().SetTitle("Cut ele Pt using PfMet using weight = 1")
	CutelePt_vs_CutPfMET_WEIGHT_ONE.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPfMET_WEIGHT_NO_K = TH2F(N+"_CutelePt_vs_CutPfMET_weight_no_k", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPfMET_WEIGHT_NO_K.GetXaxis().SetTitle("Cut PfMET using puWeight * scale1fb")
	CutelePt_vs_CutPfMET_WEIGHT_NO_K.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPfMET_WEIGHT_NO_K.GetYaxis().SetTitle("Cut ele Pt usings PfMet using puWeight * scale1fb")
	CutelePt_vs_CutPfMET_WEIGHT_NO_K.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPfMET_WEIGHT_JUST_K = TH2F(N+"_CutelePt_vs_CutPfMET_weight_just_k", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPfMET_WEIGHT_JUST_K.GetXaxis().SetTitle("Cut PfMET using kfactor * kfactorNLO")
	CutelePt_vs_CutPfMET_WEIGHT_JUST_K.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPfMET_WEIGHT_JUST_K.GetYaxis().SetTitle("Cut ele Pt usings PfMet using kfactor * kfactorNLO")
	CutelePt_vs_CutPfMET_WEIGHT_JUST_K.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPfMET_WEIGHT_ALL = TH2F(N+"_CutelePt_vs_CutPfMET_weight_all", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPfMET_WEIGHT_ALL.GetXaxis().SetTitle("Cut PfMET using puWeight * scale1fb * kfactor * kfactorNLO")
	CutelePt_vs_CutPfMET_WEIGHT_ALL.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPfMET_WEIGHT_ALL.GetYaxis().SetTitle("Cut ele Pt usings PfMet using puWeight * scale1fb * kfactor * kfactorNLO")
	CutelePt_vs_CutPfMET_WEIGHT_ALL.GetYaxis().SetTitleSize(0.045)
	#	
	CutelePt_vs_CutPfMET_WEIGHT_NEW = TH2F(N+"_CutelePt_vs_CutPfMET_weight_new", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPfMET_WEIGHT_NEW.GetXaxis().SetTitle("Cut PfMET using evtWeight")
	CutelePt_vs_CutPfMET_WEIGHT_NEW.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPfMET_WEIGHT_NEW.GetYaxis().SetTitle("Cut ele Pt usings PfMet using evtWeight")
	CutelePt_vs_CutPfMET_WEIGHT_NEW.GetYaxis().SetTitleSize(0.045)
	#	
	CutelePt_vs_CutPfMET_WEIGHT_PU = TH2F(N+"_CutelePt_vs_CutPfMET_weight_pu", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPfMET_WEIGHT_PU.GetXaxis().SetTitle("Cut PfMET using puWeight")
	CutelePt_vs_CutPfMET_WEIGHT_PU.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPfMET_WEIGHT_PU.GetYaxis().SetTitle("Cut ele Pt usings PfMet using puWeight")
	CutelePt_vs_CutPfMET_WEIGHT_PU.GetYaxis().SetTitleSize(0.045)
	#	
	CuteleMt_vs_CutJetPt_Pf = TH2F(N+"_Cut_eleMt_vs_Cut_JetPt_Pf", "", 500, 0, 1000, 100, 0, 1000)
	CuteleMt_vs_CutJetPt_Pf.GetXaxis().SetTitle("Cut Jet Pt with ele cuts using PfMet")
	CuteleMt_vs_CutJetPt_Pf.GetXaxis().SetTitleSize(0.045)
	CuteleMt_vs_CutJetPt_Pf.GetYaxis().SetTitle("Cut ele Mt using PfMet")
	CuteleMt_vs_CutJetPt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutElePhi_Pf = TH2F(N+"_CutJetPhi_vs_CutElePhi_Pf", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutElePhi_Pf.GetXaxis().SetTitle("Cut Ele Phi using PfMet")
	CutJetPhi_vs_CutElePhi_Pf.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutElePhi_Pf.GetYaxis().SetTitle("Cut Jet Phi with ele cuts using PfMet")
	CutJetPhi_vs_CutElePhi_Pf.GetYaxis().SetTitleSize(0.045)
	#
	CutElePhi_vs_CutPfMetPhi = TH2F(N+"_CutElePhi_vs_CutPfMetPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutElePhi_vs_CutPfMetPhi.GetXaxis().SetTitle("Cut PfMet Phi with ele cuts")
	CutElePhi_vs_CutPfMetPhi.GetXaxis().SetTitleSize(0.045)
	CutElePhi_vs_CutPfMetPhi.GetYaxis().SetTitle("Cut Ele Phi using PfMet")
	CutElePhi_vs_CutPfMetPhi.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutPfMetPhi_e = TH2F(N+"_CutJetPhi_vs_PfMetPhi_e", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutPfMetPhi_e.GetXaxis().SetTitle("Cut PfMet Phi with ele cuts")
	CutJetPhi_vs_CutPfMetPhi_e.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutPfMetPhi_e.GetYaxis().SetTitle("Cut Jet Phi with ele cuts using PfMet")
	CutJetPhi_vs_CutPfMetPhi_e.GetYaxis().SetTitleSize(0.045)
	#
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_elePt = TH2F(N+"_Cut_atan_pfmet_over_elePt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetXaxis().SetTitle("Cut_Delta R of AK4_1") 
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetXaxis().SetTitleSize(0.045)
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetYaxis().SetTitle("Cut_Angle of pi/4 - atan(pfmet/elePt)")
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_elePt.GetYaxis().SetTitleSize(0.045)


#Muon PfMet
#        folder3.cd()
	#
	Cut_Jet_Mass_m_Pf_0 = TH1F(N+"_Cut_Jet_Mass_m_Pf_0", "", 80, 0, 400)
        Cut_Jet_Mass_m_Pf_0.GetXaxis().SetTitle("Leading AK8 Jet Mass muo cuts using PfMet (GeV)")
        Cut_Jet_Mass_m_Pf_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Mass_m_Pf_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Mass_m_Pf_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Jet_Phi_m_Pf_0 = TH1F(N+"_Cut_Jet_Phi_m_Pf_0", "", 100, -3.7, 3.7)
        Cut_Jet_Phi_m_Pf_0.GetXaxis().SetTitle("Leading AK8 Jet #phi muo cuts using PfMet")
        Cut_Jet_Phi_m_Pf_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Phi_m_Pf_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Phi_m_Pf_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Jet_Eta_m_Pf_0 = TH1F(N+"_Cut_Jet_Eta_m_Pf_0", "", 60, -3, 3)
        Cut_Jet_Eta_m_Pf_0.GetXaxis().SetTitle("Leading Jet #eta muo cuts using PfMet")
        Cut_Jet_Eta_m_Pf_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Eta_m_Pf_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Eta_m_Pf_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_NJets_m_Pf = TH1F(N + "_Cut_NJets_m_Pf", "", 6, 0, 6)
        Cut_NJets_m_Pf.GetXaxis().SetTitle("Number of Jets muo cuts using PfMet")
        Cut_NJets_m_Pf.GetXaxis().SetTitleSize(0.045)
        Cut_NJets_m_Pf.GetYaxis().SetTitle("Events")
        Cut_NJets_m_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Npv_m_Pf = TH1F(N+"_Cut_Npv_m", "", 180, 0, 90) 
        Cut_Npv_m_Pf.GetXaxis().SetTitle("Number of Primary Vertices muo cuts using PfMet")
        Cut_Npv_m_Pf.GetXaxis().SetTitleSize(0.045)
        Cut_Npv_m_Pf.GetYaxis().SetTitle("Events")
        Cut_Npv_m_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PfMet_Phi_m = TH1F(N+"_Cut_PfMet_phi_m", "", 100, -3.7, 3.7)
	Cut_PfMet_Phi_m.GetXaxis().SetTitle("PfMet phi muo cut")
	Cut_PfMet_Phi_m.GetXaxis().SetTitleSize(0.045)
	Cut_PfMet_Phi_m.GetYaxis().SetTitle("Events")
	Cut_PfMet_Phi_m.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PfMet_m = TH1F(N+"_Cut_PfMet_m", "", 200, 0, 1000)
        Cut_PfMet_m.GetXaxis().SetTitle("pf MET muo cuts")
        Cut_PfMet_m.GetXaxis().SetTitleSize(0.045)
        Cut_PfMet_m.GetYaxis().SetTitle("Events")
        Cut_PfMet_m.GetYaxis().SetTitleSize(0.045)
	#
	Cut_muo_pt_Pf = TH1F(N+"_Cut_muo_pt_Pf", "", 200, 0, 1000)
	Cut_muo_pt_Pf.GetXaxis().SetTitle("Cut muo pt using PfMet")
	Cut_muo_pt_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_muo_pt_Pf.GetYaxis().SetTitle("Events")
	Cut_muo_pt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_muo_phi_Pf = TH1F(N+"_Cut_muo_phi_Pf", "", 100, -3.7, 3.7)
	Cut_muo_phi_Pf.GetXaxis().SetTitle("Cut muo phi using PfMet")
	Cut_muo_phi_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_muo_phi_Pf.GetYaxis().SetTitle("Events")
	Cut_muo_phi_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_muo_eta_Pf = TH1F(N+"_Cut_muo_eta_Pf", "", 60, -3, -3)
	Cut_muo_eta_Pf.GetXaxis().SetTitle("Cut muo eta using PfMet")
	Cut_muo_eta_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_muo_eta_Pf.GetYaxis().SetTitle("Events")
	Cut_muo_eta_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Mt_Muo_Pf = TH1F(N+"_Cut_Mt_Muo_Pf", "", 500, 0, 1000)
	Cut_Mt_Muo_Pf.GetXaxis().SetTitle("Cut Mt Muo using PfMet")
	Cut_Mt_Muo_Pf.GetXaxis().SetTitleSize(0.045)
	Cut_Mt_Muo_Pf.GetYaxis().SetTitle("Events")
	Cut_Mt_Muo_Pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_0_pf = TH1F(N + "_Cut_delta_R_muo_AK4_0_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_0_pf.GetXaxis().SetTitle("delta R for muon and AK4_0 with pfmet cuts")
	Cut_delta_R_muo_AK4_0_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_0_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_0_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_1_pf = TH1F(N + "_Cut_delta_R_muo_AK4_1_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_1_pf.GetXaxis().SetTitle("delta R for muon and AK4_1 with pfmet cuts")
	Cut_delta_R_muo_AK4_1_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_1_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_1_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_2_pf = TH1F(N + "_Cut_delta_R_muo_AK4_2_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_2_pf.GetXaxis().SetTitle("delta R for muon and AK4_2 with pfmet cuts")
	Cut_delta_R_muo_AK4_2_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_2_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_2_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_3_pf = TH1F(N + "_Cutdelta_R_muo_AK4_3_pf", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_3_pf.GetXaxis().SetTitle("delta R for muon and AK4_3 with pfmet cuts")
	Cut_delta_R_muo_AK4_3_pf.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_3_pf.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_3_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Low_angle_muoPt_over_pfmet = TH1F(N + "_Cut_low_angle_muoPt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_Low_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Cut Angle between MuoPt and PfMet")
	Cut_Low_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_Low_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Events")
	Cut_Low_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#				    
	Cut_High_angle_muoPt_over_pfmet = TH1F(N + "_Cut_high_angle_muoPt_over_pfmet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_High_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Cut Angle from midline between MuoPt and PfMet")
	Cut_High_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_High_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Events")
	Cut_High_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#				    	
	CutJetPt_vs_CutmuoPt_Pf = TH2F(N+"_CutJetPt_vs_CutmuoPt_Pf", "", 200, 0, 1000, 200, 0, 1000)
	CutJetPt_vs_CutmuoPt_Pf.GetXaxis().SetTitle("Cut muo Pt using PfMet")
	CutJetPt_vs_CutmuoPt_Pf.GetXaxis().SetTitleSize(0.045)
	CutJetPt_vs_CutmuoPt_Pf.GetYaxis().SetTitle("Cut Jet Pt with muo cuts using PfMet")
	CutJetPt_vs_CutmuoPt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPfMET_WEIGHT_ONE = TH2F(N+"_CutmuoPt_vs_CutPfMET_weight_one", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPfMET_WEIGHT_ONE.GetXaxis().SetTitle("Cut PfMET using weight=1")
	CutmuoPt_vs_CutPfMET_WEIGHT_ONE.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPfMET_WEIGHT_ONE.GetYaxis().SetTitle("Cut muo Pt using PfMet using weight=1")
	CutmuoPt_vs_CutPfMET_WEIGHT_ONE.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPfMET_WEIGHT_NO_K = TH2F(N+"_CutmuoPt_vs_CutPfMET_weight_no_k", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPfMET_WEIGHT_NO_K.GetXaxis().SetTitle("Cut PfMET using puWeight * scale1fb")
	CutmuoPt_vs_CutPfMET_WEIGHT_NO_K.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPfMET_WEIGHT_NO_K.GetYaxis().SetTitle("Cut muo Pt using PfMet using puWeight * scale1fb")
	CutmuoPt_vs_CutPfMET_WEIGHT_NO_K.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPfMET_WEIGHT_JUST_K = TH2F(N+"_CutmuoPt_vs_CutPfMET_weight_just_k", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPfMET_WEIGHT_JUST_K.GetXaxis().SetTitle("Cut PfMET using kfactor * kfactorNLO")
	CutmuoPt_vs_CutPfMET_WEIGHT_JUST_K.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPfMET_WEIGHT_JUST_K.GetYaxis().SetTitle("Cut muo Pt using PfMet using kfactor * kfactorNLO")
	CutmuoPt_vs_CutPfMET_WEIGHT_JUST_K.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPfMET_WEIGHT_ALL = TH2F(N+"_CutmuoPt_vs_CutPfMET_weight_all", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPfMET_WEIGHT_ALL.GetXaxis().SetTitle("Cut PfMET using puWeight * scale1fb * kfactor * kfactorNLO")
	CutmuoPt_vs_CutPfMET_WEIGHT_ALL.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPfMET_WEIGHT_ALL.GetYaxis().SetTitle("Cut muo Pt using PfMet")
	CutmuoPt_vs_CutPfMET_WEIGHT_ALL.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPfMET_WEIGHT_NEW = TH2F(N+"_CutmuoPt_vs_CutPfMET_weight_new", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPfMET_WEIGHT_NEW.GetXaxis().SetTitle("Cut PfMET using evtWeight")
	CutmuoPt_vs_CutPfMET_WEIGHT_NEW.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPfMET_WEIGHT_NEW.GetYaxis().SetTitle("Cut muo Pt using pfMet using evtWeight")
	CutmuoPt_vs_CutPfMET_WEIGHT_NEW.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPfMET_WEIGHT_PU = TH2F(N+"_CutmuoPt_vs_CutPfMET_weight_pu", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPfMET_WEIGHT_PU.GetXaxis().SetTitle("Cut PfMET using puWeight")
	CutmuoPt_vs_CutPfMET_WEIGHT_PU.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPfMET_WEIGHT_PU.GetYaxis().SetTitle("Cut muo Pt using pfMet using puWeight")
	CutmuoPt_vs_CutPfMET_WEIGHT_PU.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoMt_vs_CutJetPt_Pf = TH2F(N+"_Cut_muoMt_vs_Cut_JetPt_Pf", "", 500, 0, 1000, 100, 0, 1000)
	CutmuoMt_vs_CutJetPt_Pf.GetXaxis().SetTitle("Cut Jet Pt with muo cuts using PfMet")
	CutmuoMt_vs_CutJetPt_Pf.GetXaxis().SetTitleSize(0.045)
	CutmuoMt_vs_CutJetPt_Pf.GetYaxis().SetTitle("Cut muo Mt using PfMet")
	CutmuoMt_vs_CutJetPt_Pf.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutMuoPhi_Pf = TH2F(N+"_CutJetPhi_vs_CutMuoPhi_Pf", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutMuoPhi_Pf.GetXaxis().SetTitle("Cut Muo Phi using PfMet")
	CutJetPhi_vs_CutMuoPhi_Pf.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutMuoPhi_Pf.GetYaxis().SetTitle("Cut Jet Phi with muo cuts using PfMet")
	CutJetPhi_vs_CutMuoPhi_Pf.GetYaxis().SetTitleSize(0.045)
	#
	CutMuoPhi_vs_CutPfMetPhi = TH2F(N+"_CutMuoPhi_vs_CutPfMetPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutMuoPhi_vs_CutPfMetPhi.GetXaxis().SetTitle("Cut PfMet Phi with muo cuts")
	CutMuoPhi_vs_CutPfMetPhi.GetXaxis().SetTitleSize(0.045)
	CutMuoPhi_vs_CutPfMetPhi.GetYaxis().SetTitle("Cut Muo Phi using PfMet")
	CutMuoPhi_vs_CutPfMetPhi.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutPfMetPhi_m = TH2F(N+"_CutJetPhi_vs_PfMetPhi_m", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutPfMetPhi_m.GetXaxis().SetTitle("Cut PfMet Phi with muo cuts")
	CutJetPhi_vs_CutPfMetPhi_m.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutPfMetPhi_m.GetYaxis().SetTitle("Cut Jet Phi with muo cuts using PfMet")
	CutJetPhi_vs_CutPfMetPhi_e.GetYaxis().SetTitleSize(0.045)
	#
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_muoPt = TH2F(N+"_Cut_atan_pfmet_over_muoPt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetXaxis().SetTitle("Cut Delta R of AK4_1") 
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetXaxis().SetTitleSize(0.045)
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(pfmet/muoPt)")
#	Cut_deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.GetYaxis().SetTitleSize(0.045)



#Electron Cuts wiht Puppi Met (defining Histograms)

#        folder4.cd()
	#
	Cut_Jet_Mass_e_Puppi_0 = TH1F(N+"_Cut_Jet_Mass_e_Puppi_0", "", 80, 0, 400)
        Cut_Jet_Mass_e_Puppi_0.GetXaxis().SetTitle("Leading AK8 Jet Mass ele cuts using PuppiMet(GeV)")
        Cut_Jet_Mass_e_Puppi_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Mass_e_Puppi_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Mass_e_Puppi_0.GetYaxis().SetTitleSize(0.045)
	#
        Cut_Jet_Phi_e_Puppi_0 = TH1F(N+"_Cut_Jet_Phi_e_Puppi_0", "", 100, -3.7, 3.7)
        Cut_Jet_Phi_e_Puppi_0.GetXaxis().SetTitle("Leading AK8 Jet #phi ele cuts using PuppiMet")
        Cut_Jet_Phi_e_Puppi_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Phi_e_Puppi_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Phi_e_Puppi_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Jet_Eta_e_Puppi_0 = TH1F(N+"_Cut_Jet_Eta_e_Puppi_0", "", 60, -3, 3)
        Cut_Jet_Eta_e_Puppi_0.GetXaxis().SetTitle("Leading Jet #eta ele cuts using PuppiMet")
        Cut_Jet_Eta_e_Puppi_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Eta_e_Puppi_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Eta_e_Puppi_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_NJets_e_Puppi = TH1F(N + "_Cut_NJets_e_Puppi", "", 6, 0, 6)
        Cut_NJets_e_Puppi.GetXaxis().SetTitle("Number of Jets ele cuts using PuppiMet")
        Cut_NJets_e_Puppi.GetXaxis().SetTitleSize(0.045)
        Cut_NJets_e_Puppi.GetYaxis().SetTitle("Events")
        Cut_NJets_e_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Npv_e_Puppi = TH1F(N+"_Cut_Npv_e_Puppi", "", 180, 0, 90) 
        Cut_Npv_e_Puppi.GetXaxis().SetTitle("Number of Primary Vertices ele cuts using PuppiMet")
        Cut_Npv_e_Puppi.GetXaxis().SetTitleSize(0.045)
        Cut_Npv_e_Puppi.GetYaxis().SetTitle("Events")
        Cut_Npv_e_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PuppiMet_Phi_e = TH1F(N+"_Cut_PuppiMet_phi_e", "", 100, -3.7, 3.7)
	Cut_PuppiMet_Phi_e.GetXaxis().SetTitle("PuppiMet phi ele cuts")
	Cut_PuppiMet_Phi_e.GetXaxis().SetTitleSize(0.045)
	Cut_PuppiMet_Phi_e.GetYaxis().SetTitle("Events")
	Cut_PuppiMet_Phi_e.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PuppiMet_e = TH1F(N+"_Cut_PuppiMet_e", "", 200, 0, 1000)
        Cut_PuppiMet_e.GetXaxis().SetTitle("Puppi MET ele cuts")
        Cut_PuppiMet_e.GetXaxis().SetTitleSize(0.045)
        Cut_PuppiMet_e.GetYaxis().SetTitle("Events")
        Cut_PuppiMet_e.GetYaxis().SetTitleSize(0.045)
	#
	Cut_ele_pt_Puppi = TH1F(N+"_Cut_ele_pt_Puppi", "", 200, 0, 1000)
	Cut_ele_pt_Puppi.GetXaxis().SetTitle("Cut ele pt using PuppiMet")
	Cut_ele_pt_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_ele_pt_Puppi.GetYaxis().SetTitle("Events")
	Cut_ele_pt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_ele_phi_Puppi = TH1F(N+"_Cut_ele_phi_Puppi", "", 100, -3.7, 3.7)
	Cut_ele_phi_Puppi.GetXaxis().SetTitle("Cut ele phi using PuppiMet")
	Cut_ele_phi_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_ele_phi_Puppi.GetYaxis().SetTitle("Events")
	Cut_ele_phi_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_ele_eta_Puppi = TH1F(N+"_Cut_ele_eta_Puppi", "", 60, -3, 3)
	Cut_ele_eta_Puppi.GetXaxis().SetTitle("Cut ele eta using PuppiMet")
	Cut_ele_eta_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_ele_eta_Puppi.GetYaxis().SetTitle("Events")
	Cut_ele_eta_Puppi.GetYaxis().SetTitleSize(0.045)	
	#
	Cut_Mt_Ele_Puppi = TH1F(N+"_Cut_Mt_Ele_Puppi", "", 500, 0, 1000)
	Cut_Mt_Ele_Puppi.GetXaxis().SetTitle("Cut Mt Ele using PuppiMet")
	Cut_Mt_Ele_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_Mt_Ele_Puppi.GetYaxis().SetTitle("Events")
	Cut_Mt_Ele_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_0_puppi = TH1F(N + "delta_R_ele_AK4_0_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_0_puppi.GetXaxis().SetTitle("delta R for electron and AK4_0 with puppet cuts")
	Cut_delta_R_ele_AK4_0_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_0_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_0_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_1_puppi = TH1F(N + "Cut_delta_R_ele_AK4_1_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_1_puppi.GetXaxis().SetTitle("delta R for electron and AK4_1 with puppet cuts")
	Cut_delta_R_ele_AK4_1_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_1_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_1_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_2_puppi = TH1F(N + "Cut_delta_R_ele_AK4_2_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_2_puppi.GetXaxis().SetTitle("delta R for electron and AK4_2 with puppet cuts")
	Cut_delta_R_ele_AK4_2_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_2_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_2_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_ele_AK4_3_puppi = TH1F(N + "Cut_delta_R_ele_AK4_3_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_ele_AK4_3_puppi.GetXaxis().SetTitle("delta R for electron and AK4_3 with puppet cuts")
	Cut_delta_R_ele_AK4_3_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_ele_AK4_3_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_ele_AK4_3_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Low_angle_elePt_over_puppet = TH1F(N + "_Cut_low_angle_elePt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_Low_angle_elePt_over_puppet.GetXaxis().SetTitle("Cut Angle between ElePt and Puppet")
	Cut_Low_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_Low_angle_elePt_over_puppet.GetYaxis().SetTitle("Events")
	Cut_Low_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_High_angle_elePt_over_puppet = TH1F(N + "_Cut_high_angle_elePt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_High_angle_elePt_over_puppet.GetXaxis().SetTitle("Cut Angle from midline between ElePt and Puppet")
	Cut_High_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_High_angle_elePt_over_puppet.GetYaxis().SetTitle("Events")
	Cut_High_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPt_vs_CutelePt_Puppi = TH2F(N+"_CutJetPt_vs_CutelePt_Puppi", "", 200, 0, 1000, 200, 0, 1000)
	CutJetPt_vs_CutelePt_Puppi.GetXaxis().SetTitle("Cut ele Pt using PuppiMet")
	CutJetPt_vs_CutelePt_Puppi.GetXaxis().SetTitleSize(0.045)
	CutJetPt_vs_CutelePt_Puppi.GetYaxis().SetTitle("Cut Jet Pt with ele cuts using PuppiMet")
	CutJetPt_vs_CutelePt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPuppiMET_WEIGHT_ONE = TH2F(N+"_CutelePt_vs_CutPuppiMET_weight_one", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPuppiMET_WEIGHT_ONE.GetXaxis().SetTitle("Cut PuppiMET using weight=1")
	CutelePt_vs_CutPuppiMET_WEIGHT_ONE.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPuppiMET_WEIGHT_ONE.GetYaxis().SetTitle("Cut ele Pt using PuppiMet using weight=1")
	CutelePt_vs_CutPuppiMET_WEIGHT_ONE.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPuppiMET_WEIGHT_NO_K = TH2F(N+"_CutelePt_vs_CutPuppiMET_weight_no_k", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPuppiMET_WEIGHT_NO_K.GetXaxis().SetTitle("Cut PuppiMET using puWeight * scalbe1fb")
	CutelePt_vs_CutPuppiMET_WEIGHT_NO_K.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPuppiMET_WEIGHT_NO_K.GetYaxis().SetTitle("Cut ele Pt using PuppiMet using puWeight * scale1fb")
	CutelePt_vs_CutPuppiMET_WEIGHT_NO_K.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPuppiMET_WEIGHT_JUST_K = TH2F(N+"_CutelePt_vs_CutPuppiMET_weight_just_k", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPuppiMET_WEIGHT_JUST_K.GetXaxis().SetTitle("Cut PuppiMET using kfactor * kfactorNLO")
	CutelePt_vs_CutPuppiMET_WEIGHT_JUST_K.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPuppiMET_WEIGHT_JUST_K.GetYaxis().SetTitle("Cut ele Pt using PuppiMet using kfactor * kfactorNLO")
	CutelePt_vs_CutPuppiMET_WEIGHT_JUST_K.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPuppiMET_WEIGHT_ALL = TH2F(N+"_CutelePt_vs_CutPuppiMET_weight_all", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPuppiMET_WEIGHT_ALL.GetXaxis().SetTitle("Cut PuppiMET using puWeight * scale1fb * kfactor * kfactorNLO")
	CutelePt_vs_CutPuppiMET_WEIGHT_ALL.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPuppiMET_WEIGHT_ALL.GetYaxis().SetTitle("Cut ele Pt using PuppiMet using puWeight * scale1fb *kfactor * kfactorNLO")
	CutelePt_vs_CutPuppiMET_WEIGHT_ALL.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPuppiMET_WEIGHT_NEW = TH2F(N+"_CutelePt_vs_CutPuppiMET_weight_new", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPuppiMET_WEIGHT_NEW.GetXaxis().SetTitle("Cut PuppiMET using evtWeight")
	CutelePt_vs_CutPuppiMET_WEIGHT_NEW.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPuppiMET_WEIGHT_NEW.GetYaxis().SetTitle("Cut ele Pt using PuppiMet using evtWeight")
	CutelePt_vs_CutPuppiMET_WEIGHT_NEW.GetYaxis().SetTitleSize(0.045)
	#
	CutelePt_vs_CutPuppiMET_WEIGHT_PU = TH2F(N+"_CutelePt_vs_CutPuppiMET_weight_pu", "", 200, 0, 1000, 200, 0, 1000)
	CutelePt_vs_CutPuppiMET_WEIGHT_PU.GetXaxis().SetTitle("Cut PuppiMET using puWeight")
	CutelePt_vs_CutPuppiMET_WEIGHT_PU.GetXaxis().SetTitleSize(0.045)
	CutelePt_vs_CutPuppiMET_WEIGHT_PU.GetYaxis().SetTitle("Cut ele Pt using PuppiMet using puWeight")
	CutelePt_vs_CutPuppiMET_WEIGHT_PU.GetYaxis().SetTitleSize(0.045)
	#
	CuteleMt_vs_CutJetPt_Puppi = TH2F(N+"_Cut_eleMt_vs_Cut_JetPt_Puppi", "", 500, 0, 1000, 100, 0, 1000)
	CuteleMt_vs_CutJetPt_Puppi.GetXaxis().SetTitle("Cut Jet Pt using PuppiMet")
	CuteleMt_vs_CutJetPt_Puppi.GetXaxis().SetTitleSize(0.045)
	CuteleMt_vs_CutJetPt_Puppi.GetYaxis().SetTitle("Cut ele Mt using PuppiMet")
	CuteleMt_vs_CutJetPt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutElePhi_Puppi = TH2F(N+"_CutJetPhi_vs_CutElePhi_Puppi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutElePhi_Puppi.GetXaxis().SetTitle("Cut Ele Phi using PuppiMet")
	CutJetPhi_vs_CutElePhi_Puppi.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutElePhi_Puppi.GetYaxis().SetTitle("Cut Jet Phi with ele cuts using PuppiMet")
	CutJetPhi_vs_CutElePhi_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	CutElePhi_vs_CutPuppiMetPhi = TH2F(N+"_CutElePhi_vs_CutPuppiMetPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutElePhi_vs_CutPuppiMetPhi.GetXaxis().SetTitle("Cut PuppiMet Phi with ele cuts")
	CutElePhi_vs_CutPuppiMetPhi.GetXaxis().SetTitleSize(0.045)
	CutElePhi_vs_CutPuppiMetPhi.GetYaxis().SetTitle("Cut Ele Phi using PuppiMet")
	CutElePhi_vs_CutPuppiMetPhi.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutPuppiMetPhi_e = TH2F(N+"_CutJetPh_vs_PuppiMetPhi_e", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutPuppiMetPhi_e.GetXaxis().SetTitle("Cut PuppiMet Phi with ele cuts")
	CutJetPhi_vs_CutPuppiMetPhi_e.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutPuppiMetPhi_e.GetYaxis().SetTitle("Cut Jet Phi with ele cuts using PuppiMet")
	CutJetPhi_vs_CutPuppiMetPhi_e.GetYaxis().SetTitleSize(0.045)
	#
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_elePt = TH2F(N+"_Cut_atan_puppet_over_elePt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetXaxis().SetTitle("Cut Delta R of AK4_1") 
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetXaxis().SetTitleSize(0.045)
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(puppet/elePt)")
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_elePt.GetYaxis().SetTitleSize(0.045)
	#

#Muon Cuts with Puppi Met (defining Histograms)
#        folder5.cd()
	#
	Cut_Jet_Mass_m_Puppi_0 = TH1F(N+"_Cut_Jet_Mass_m_Puppi_0", "", 80, 0, 400)
        Cut_Jet_Mass_m_Puppi_0.GetXaxis().SetTitle("Leading AK8 Jet Mass muo cuts using PuppiMet(GeV)")
        Cut_Jet_Mass_m_Puppi_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Mass_m_Puppi_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Mass_m_Puppi_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Jet_Phi_m_Puppi_0 = TH1F(N+"_Cut_Jet_Phi_m_Puppi_0", "", 100, -3.7, 3.7)
        Cut_Jet_Phi_m_Puppi_0.GetXaxis().SetTitle("Leading AK8 Jet #phi muo cuts using PuppiMet")
        Cut_Jet_Phi_m_Puppi_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Phi_m_Puppi_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Phi_m_Puppi_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Jet_Eta_m_Puppi_0 = TH1F(N+"_Cut_Jet_Eta_m_Puppi_0", "", 60, -3, 3)
        Cut_Jet_Eta_m_Puppi_0.GetXaxis().SetTitle("Leading Jet #eta muo cuts using PuppiMet")
        Cut_Jet_Eta_m_Puppi_0.GetXaxis().SetTitleSize(0.045)
        Cut_Jet_Eta_m_Puppi_0.GetYaxis().SetTitle("Events")
        Cut_Jet_Eta_m_Puppi_0.GetYaxis().SetTitleSize(0.045)
	#
	Cut_NJets_m_Puppi = TH1F(N + "_Cut_NJets_m_Puppi", "", 6, 0, 6)
        Cut_NJets_m_Puppi.GetXaxis().SetTitle("Number of Jets muo cuts using PuppiMet")
        Cut_NJets_m_Puppi.GetXaxis().SetTitleSize(0.045)
        Cut_NJets_m_Puppi.GetYaxis().SetTitle("Events")
        Cut_NJets_m_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Npv_m_Puppi = TH1F(N+"_Cut_Npv_m_Puppi", "", 180, 0, 90) 
        Cut_Npv_m_Puppi.GetXaxis().SetTitle("Number of Primary Vertices muo cuts using PuppiMet")
        Cut_Npv_m_Puppi.GetXaxis().SetTitleSize(0.045)
        Cut_Npv_m_Puppi.GetYaxis().SetTitle("Events")
        Cut_Npv_m_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PuppiMet_Phi_m = TH1F(N+"_PuppiMet_phi_m", "", 100, -3.7, 3.7)
	Cut_PuppiMet_Phi_m.GetXaxis().SetTitle("PuppiMet phi muo cuts")
	Cut_PuppiMet_Phi_m.GetXaxis().SetTitleSize(0.045)
	Cut_PuppiMet_Phi_m.GetYaxis().SetTitle("Events")
	Cut_PuppiMet_Phi_m.GetYaxis().SetTitleSize(0.045)
	#
	Cut_PuppiMet_m = TH1F(N+"_Cut_PuppiMet_m", "", 200, 0, 1000)
        Cut_PuppiMet_m.GetXaxis().SetTitle("Puppi MET muo cuts")
        Cut_PuppiMet_m.GetXaxis().SetTitleSize(0.045)
        Cut_PuppiMet_m.GetYaxis().SetTitle("Events")
        Cut_PuppiMet_m.GetYaxis().SetTitleSize(0.045)
	#
	Cut_muo_pt_Puppi = TH1F(N+"_Cut_muo_pt_Puppi", "", 200, 0, 1000)
	Cut_muo_pt_Puppi.GetXaxis().SetTitle("Cut muo pt using PuppiMet")
	Cut_muo_pt_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_muo_pt_Puppi.GetYaxis().SetTitle("Events")
	Cut_muo_pt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_muo_phi_Puppi = TH1F(N+"_Cut_muo_phi_Puppi", "", 100, -3.7, 3.7)
	Cut_muo_phi_Puppi.GetXaxis().SetTitle("Cut muo phi using PuppiMet")
	Cut_muo_phi_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_muo_phi_Puppi.GetYaxis().SetTitle("Events")
	Cut_muo_phi_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_muo_eta_Puppi = TH1F(N+"_Cut_muo_eta_Puppi", "", 60, -3, -3)
	Cut_muo_eta_Puppi.GetXaxis().SetTitle("Cut muo eta using PuppiMet")
	Cut_muo_eta_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_muo_eta_Puppi.GetYaxis().SetTitle("Events")
	Cut_muo_eta_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Mt_Muo_Puppi = TH1F(N+"_Cut_Mt_Muo_Puppi", "", 500, 0, 1000)
	Cut_Mt_Muo_Puppi.GetXaxis().SetTitle("Cut Mt Muo using PuppiMet")
	Cut_Mt_Muo_Puppi.GetXaxis().SetTitleSize(0.045)
	Cut_Mt_Muo_Puppi.GetYaxis().SetTitle("Events")
	Cut_Mt_Muo_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_0_puppi = TH1F(N + "Cut_delta_R_muo_AK4_0_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_0_puppi.GetXaxis().SetTitle("delta R for muon and AK4_0 with puppet cuts")
	Cut_delta_R_muo_AK4_0_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_0_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_0_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_1_puppi = TH1F(N + "Cut_delta_R_muo_AK4_1_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_1_puppi.GetXaxis().SetTitle("delta R for muon and AK4_1 with puppet cuts")
	Cut_delta_R_muo_AK4_1_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_1_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_1_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_2_puppi = TH1F(N + "Cut_delta_R_muo_AK4_2_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_2_puppi.GetXaxis().SetTitle("delta R for muon and AK4_2 with puppet cuts")
	Cut_delta_R_muo_AK4_2_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_2_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_2_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_delta_R_muo_AK4_3_puppi = TH1F(N + "_Cutdelta_R_muo_AK4_3_puppi", "", 50, 0, 2*TMath.Pi())
	Cut_delta_R_muo_AK4_3_puppi.GetXaxis().SetTitle("delta R for muon and AK4_3 with puppet cuts")
	Cut_delta_R_muo_AK4_3_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_delta_R_muo_AK4_3_puppi.GetYaxis().SetTitle("Events")
	Cut_delta_R_muo_AK4_3_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_Low_angle_muoPt_over_puppet = TH1F(N + "_Cut_low_angle_muoPt_over_uppett", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_Low_angle_muoPt_over_puppet.GetXaxis().SetTitle("Cut Angle between MuoPt and puppet")
	Cut_Low_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_Low_angle_muoPt_over_puppet.GetYaxis().SetTitle("Events")
	Cut_Low_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#				    
	Cut_High_angle_muoPt_over_puppet = TH1F(N + "_Cut_high_angle_muoPt_over_puppet", "", 50, -TMath.Pi(), TMath.Pi())
	Cut_High_angle_muoPt_over_puppet.GetXaxis().SetTitle("Cut Angle from midline between MuoPt and puppet")
	Cut_High_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_High_angle_muoPt_over_puppet.GetYaxis().SetTitle("Events")
	Cut_High_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#				    
	CutJetPt_vs_CutmuoPt_Puppi = TH2F(N+"_CutJetPt_vs_CutmuoPt_Puppi", "", 200, 0, 1000, 200, 0, 1000)
	CutJetPt_vs_CutmuoPt_Puppi.GetXaxis().SetTitle("Cut muo Pt using PuppiMet")
	CutJetPt_vs_CutmuoPt_Puppi.GetXaxis().SetTitleSize(0.045)
	CutJetPt_vs_CutmuoPt_Puppi.GetYaxis().SetTitle("Cut Jet Pt with muo cuts using PuppiMet")
	CutJetPt_vs_CutmuoPt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ONE = TH2F(N+"_CutmuoPt_vs_CutPuppiMET_weight_one", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ONE.GetXaxis().SetTitle("Cut PuppiMET using weight=1")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ONE.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ONE.GetYaxis().SetTitle("Cut muo Pt using PuppiMet using weight=1")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ONE.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NO_K = TH2F(N+"_CutmuoPt_vs_CutPuppiMET_weight_no_k", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NO_K.GetXaxis().SetTitle("Cut PuppiMET using puWeight * scale1fb")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NO_K.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NO_K.GetYaxis().SetTitle("Cut muo Pt using PuppiMet using puWeight * scale1fb")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NO_K.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPuppiMET_WEIGHT_JUST_K = TH2F(N+"_CutmuoPt_vs_CutPuppiMET_weight_just_k", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_JUST_K.GetXaxis().SetTitle("Cut PuppiMET using kfactor * kfactorNLO")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_JUST_K.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_JUST_K.GetYaxis().SetTitle("Cut muo Pt using PuppiMet using kfactor * kfactorNLO")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_JUST_K.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ALL = TH2F(N+"_CutmuoPt_vs_CutPuppiMET_weight_all", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ALL.GetXaxis().SetTitle("Cut PuppiMTE using puWeight * scale1fb * kfactor * kfactorNLO")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ALL.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ALL.GetYaxis().SetTitle("Cut muo Pt using PuppiMet using puWeight * scale1fb * kfactor * kfactorNLO")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_ALL.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NEW = TH2F(N+"_CutmuoPt_vs_CutPuppiMET_weight_new", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NEW.GetXaxis().SetTitle("Cut PuppiMTE using evtWeight")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NEW.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NEW.GetYaxis().SetTitle("Cut muo Pt using PuppiMet using using evtWeight")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_NEW.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoPt_vs_CutPuppiMET_WEIGHT_PU = TH2F(N+"_CutmuoPt_vs_CutPuppiMET_weight_pu", "", 200, 0, 1000, 200, 0, 1000)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_PU.GetXaxis().SetTitle("Cut PuppiMTE using puWeight")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_PU.GetXaxis().SetTitleSize(0.045)
	CutmuoPt_vs_CutPuppiMET_WEIGHT_PU.GetYaxis().SetTitle("Cut muo Pt using PuppiMet using using puWeight")
	CutmuoPt_vs_CutPuppiMET_WEIGHT_PU.GetYaxis().SetTitleSize(0.045)
	#
	CutmuoMt_vs_CutJetPt_Puppi = TH2F(N+"_Cut_muoMt_vs_Cut_JetPt_Puppi", "", 500, 0, 1000, 100, 0, 1000)
	CutmuoMt_vs_CutJetPt_Puppi.GetXaxis().SetTitle("Cut Jet Pt with muo cuts using PuppiMet")
	CutmuoMt_vs_CutJetPt_Puppi.GetXaxis().SetTitleSize(0.045)
	CutmuoMt_vs_CutJetPt_Puppi.GetYaxis().SetTitle("Cut muo Mt using PuppiMet")
	CutmuoMt_vs_CutJetPt_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutMuoPhi_Puppi = TH2F(N+"_CutJetPhi_vs_CutMuoPhi_Puppi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutMuoPhi_Puppi.GetXaxis().SetTitle("Cut Muo Phi using PuppiMet")
	CutJetPhi_vs_CutMuoPhi_Puppi.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutMuoPhi_Puppi.GetYaxis().SetTitle("Cut Jet Phi with muo cuts using PuppiMet")
	CutJetPhi_vs_CutMuoPhi_Puppi.GetYaxis().SetTitleSize(0.045)
	#
	CutMuoPhi_vs_CutPuppiMetPhi = TH2F(N+"_CutMuoPhi_vs_CutPuppiMetPhi", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutMuoPhi_vs_CutPuppiMetPhi.GetXaxis().SetTitle("Cut PuppiMet Phi with muo cuts")
	CutMuoPhi_vs_CutPuppiMetPhi.GetXaxis().SetTitleSize(0.045)
	CutMuoPhi_vs_CutPuppiMetPhi.GetYaxis().SetTitle("Cut Muo Phi using PuppiMet")
	CutMuoPhi_vs_CutPuppiMetPhi.GetYaxis().SetTitleSize(0.045)
	#
	CutJetPhi_vs_CutPuppiMetPhi_m = TH2F(N+"_CutJetPhi_vs_PuppiMetPhi_m", "", 100, -3.7, 3.7, 100, -3.7, 3.7)
	CutJetPhi_vs_CutPuppiMetPhi_m.GetXaxis().SetTitle("Cut PuppiMet Phi with muo cuts")
	CutJetPhi_vs_CutPuppiMetPhi_m.GetXaxis().SetTitleSize(0.045)
	CutJetPhi_vs_CutPuppiMetPhi_m.GetYaxis().SetTitle("Cut Jet Phi with muo cuts using PuppiMet")
	CutJetPhi_vs_CutPuppiMetPhi_m.GetYaxis().SetTitleSize(0.045)
	#
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_muoPt = TH2F(N+"_Cut_atan_puppet_over_muoPt", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi()) 
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetXaxis().SetTitle("Cut_Delta R of AK4_1") 
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetXaxis().SetTitleSize(0.045)
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetYaxis().SetTitle("Cut_Angle of pi/4 - atan(pfmet/elePt)")
#	Cut_deltaR_AK41_vs_atan_angle_puppet_over_muoPt.GetYaxis().SetTitleSize(0.045)


#DELTA R VS ATAN LEP_PT/MET
	#
	deltaR_AK40_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_deltaR_0_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_0")
	deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/pfmet)")
	deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK41_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_deltaR_1_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_1")
	deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/pfmet)")
	deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK42_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_deltaR_2_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_2")
	deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/pfmet)")
	deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK43_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_deltaR_3_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_3")
	deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/pfmet)")
	deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK40_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_deltaR_0_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_0")
	deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/pfmet)")
	deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK41_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_deltaR_1_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_1")
	deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/pfmet)")
	deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK42_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_deltaR_2_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_2")
	deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/pfmet)")
	deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK43_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_deltaR_3_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Delta R of AK4_3")
	deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/pfmet)")
	deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK40_vs_atan_angle_elePt_over_puppet = TH2F(N+"_deltaR_0_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_0")
	deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/puppet)")
	deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK41_vs_atan_angle_elePt_over_puppet = TH2F(N+"_deltaR_1_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_1")
	deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/puppet)")
	deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK42_vs_atan_angle_elePt_over_puppet = TH2F(N+"_deltaR_2_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_2")
	deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/puppet)")
	deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK43_vs_atan_angle_elePt_over_puppet = TH2F(N+"_deltaR_3_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_3")
	deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(elePt/puppet)")
	deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK40_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_deltaR_0_vs_atan_of_muoPt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_0")
	deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/puppet)")
	deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK41_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_deltaR_1_vs_atan_of_PFMET_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_1")
	deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/puppet)")
	deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK42_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_deltaR_2_vs_atan_of_muoPt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_2")
	deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/puppet)")
	deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	deltaR_AK43_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_deltaR_3_vs_atan_of_muoPt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Delta R of AK4_3")
	deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Angle of pi/4 - atan(muoPt/puppet)")
	deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_Cut_deltaR_0_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_0")
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Cut_Angle of pi/4 - atan(elePt/pfmet)")
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_Cut_deltaR_1_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_1")
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/pfmet)")
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_Cut_deltaR_2_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_2")
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/pfmet)")
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_pfmet = TH2F(N+"_Cut_deltaR_3_vs_atan_of_elePt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_3")
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/pfmet)")
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_Cut_deltaR_0_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_0")
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/pfmet)")
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_Cut_deltaR_1_vs_atan_of_PFMET_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_1")
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/pfmet)")
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_Cut_deltaR_2_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_2")
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/pfmet)")
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_pfmet = TH2F(N+"_Cut_deltaR_3_vs_atan_of_muoPt_over_pfmet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitle("Cut Delta R of AK4_3")
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/pfmet)")
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_puppet = TH2F(N+"_Cut_deltaR_0_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_0")
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/puppet)")
	Cut_deltaR_AK40_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_puppet = TH2F(N+"_Cut_deltaR_1_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_1")
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/puppet)")
	Cut_deltaR_AK41_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_puppet = TH2F(N+"_Cut_deltaR_2_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_2")
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/puppet)")
	Cut_deltaR_AK42_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_puppet = TH2F(N+"_Cut_deltaR_3_vs_atan_of_elePt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_3")
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(elePt/puppet)")
	Cut_deltaR_AK43_vs_atan_angle_elePt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_Cut_deltaR_0_vs_atan_of_muoPt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_0")
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/puppet)")
	Cut_deltaR_AK40_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_Cut_deltaR_1_vs_atan_of_PFMET_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_1")
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/puppet)")
	Cut_deltaR_AK41_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_Cut_deltaR_2_vs_atan_of_muoPt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_2")
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/puppet)")
	Cut_deltaR_AK42_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_puppet = TH2F(N+"_Cut_deltaR_3_vs_atan_of_muoPt_over_puppet", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitle("Cut Delta R of AK4_3")
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetXaxis().SetTitleSize(0.045)
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitle("Cut Angle of pi/4 - atan(muoPt/puppet)")
	Cut_deltaR_AK43_vs_atan_angle_muoPt_over_puppet.GetYaxis().SetTitleSize(0.045)
	#
	#
	#
	DeltaR_AK4_vs_atan_elePt_over_pf = TH2F(N+"_AK4_vs_atan_elePt_over_pf", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	DeltaR_AK4_vs_atan_elePt_over_pf.GetXaxis().SetTitle("Delta R of AK4 Jet")
	DeltaR_AK4_vs_atan_elePt_over_pf.GetXaxis().SetTitleSize(0.045)
	DeltaR_AK4_vs_atan_elePt_over_pf.GetYaxis().SetTitle("Angle atan(elePt/pfMet)")
	DeltaR_AK4_vs_atan_elePt_over_pf.GetYaxis().SetTitleSize(0.045)
	#
	DeltaR_AK4_vs_atan_muoPt_over_pf = TH2F(N+"_AK4_vs_atan_muoPt_over_pf", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	DeltaR_AK4_vs_atan_muoPt_over_pf.GetXaxis().SetTitle("Delta R of AK4 Jet")
	DeltaR_AK4_vs_atan_muoPt_over_pf.GetXaxis().SetTitleSize(0.045)
	DeltaR_AK4_vs_atan_muoPt_over_pf.GetYaxis().SetTitle("Angle atan(muoPt/pfMet)")
	DeltaR_AK4_vs_atan_muoPt_over_pf.GetYaxis().SetTitleSize(0.045)
	#
	DeltaR_AK4_vs_atan_elePt_over_puppi = TH2F(N+"_AK4_vs_atan_elePt_over_puppi", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	DeltaR_AK4_vs_atan_elePt_over_puppi.GetXaxis().SetTitle("Delta R of AK4 Jet")
	DeltaR_AK4_vs_atan_elePt_over_puppi.GetXaxis().SetTitleSize(0.045)
	DeltaR_AK4_vs_atan_elePt_over_puppi.GetYaxis().SetTitle("Angle atan(elePt/puppet)")
	DeltaR_AK4_vs_atan_elePt_over_puppi.GetYaxis().SetTitleSize(0.045)
	#
	DeltaR_AK4_vs_atan_muoPt_over_puppi = TH2F(N+"_AK4_vs_atan_muoPt_over_puppi", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	DeltaR_AK4_vs_atan_muoPt_over_puppi.GetXaxis().SetTitle("Delta R of AK4 Jet")
	DeltaR_AK4_vs_atan_muoPt_over_puppi.GetXaxis().SetTitleSize(0.045)
	DeltaR_AK4_vs_atan_muoPt_over_puppi.GetYaxis().SetTitle("Angle atan(muoPt/puppet)")
	DeltaR_AK4_vs_atan_muoPt_over_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_DeltaR_AK4_vs_atan_elePt_over_pf = TH2F(N+"_Cut_AK4_vs_atan_elePt_over_pf", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_DeltaR_AK4_vs_atan_elePt_over_pf.GetXaxis().SetTitle("Cut Delta R of AK4 Jet")
	Cut_DeltaR_AK4_vs_atan_elePt_over_pf.GetXaxis().SetTitleSize(0.045)
	Cut_DeltaR_AK4_vs_atan_elePt_over_pf.GetYaxis().SetTitle("Cut Angle atan(elePt/pfMet)")
	Cut_DeltaR_AK4_vs_atan_elePt_over_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_DeltaR_AK4_vs_atan_muoPt_over_pf = TH2F(N+"_Cut_AK4_vs_atan_muoPt_over_pf", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.GetXaxis().SetTitle("Cut Delta R of AK4 Jet")
	Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.GetXaxis().SetTitleSize(0.045)
	Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.GetYaxis().SetTitle("Cut Angle atan(muoPt/pfMet)")
	Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.GetYaxis().SetTitleSize(0.045)
	#
	Cut_DeltaR_AK4_vs_atan_elePt_over_puppi = TH2F(N+"_Cut_AK4_vs_atan_elePt_over_puppi", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.GetXaxis().SetTitle("Cut Delta R of AK4 Jet")
	Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.GetYaxis().SetTitle("Cut Angle atan(elePt/puppet)")
	Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.GetYaxis().SetTitleSize(0.045)
	#
	Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi = TH2F(N+"_Cut_AK4_vs_atan_muoPt_over_puppi", "", 50, 0, 2*TMath.Pi(), 50, -TMath.Pi(), TMath.Pi())
	Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.GetXaxis().SetTitle("Cut Delta R of AK4 Jet")
	Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.GetXaxis().SetTitleSize(0.045)
	Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.GetYaxis().SetTitle("Cut Angle atan(muoPt/puppet)")
	Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.GetYaxis().SetTitleSize(0.045)


	

	infile=ROOT.TFile(F)
	T = infile.Get("Events")
#	if 'Signal' in S:
#               T = infile.Get("Events")
#	else:
#		T = infile.Get("otree")
	nent = T.GetEntries()
	print " -------------------- Starting Event Loop: " + str(nent) + " entries"
	for i in range(nent):
		T.GetEntry(i)
		if(i % (1 * nent/100) == 0):
			sys.stdout.write("\r -" + "-"*int(20*(i/nent)) + " " + str(round(100.*(i/nent),0)) + "% done")
			sys.stdout.flush()

		scale1fb = 1.0

		weight = 1.0
		weight_NO_K = T.puWeight*1.0
		weight_just_k = T.kfactor*T.kfactorNLO
		weight_all = T.puWeight*T.kfactor*T.kfactorNLO*1.0
		weight_evt = T.evtWeight
		weight_PU = T.puWeight


		Jet_0 = TLorentzVector()
		AK4Jet_0 = TLorentzVector()
		AK4Jet_1 = TLorentzVector()
		AK4Jet_2 = TLorentzVector()
		AK4Jet_3 = TLorentzVector()
		ele_distance = TLorentzVector()
		muo_distance = TLorentzVector()


	#Defining Variables
		MASS_0 = T.AK8Puppijet0_msd
		ele_mass = 0.00051
		muo_mass = 0.105
		PT_0 = T.AK8Puppijet0_pt
		M = T.AK8Puppijet0_msd
		ETA_0 = T.AK8Puppijet0_eta
		PHI_0 = T.AK8Puppijet0_phi
		NJETS = T.nAK8Puppijets		
		PFMET = T.pfmet
		PuppiMET = T.puppet
		PfMET_phi = T.pfmetphi
		PuppiMET_phi = T.puppetphi
		NPV = T.npv
		muo_pt = T.vmuoLoose0_pt
		muo_eta = T.vmuoLoose0_eta
		muo_phi = T.vmuoLoose0_phi
		ele_pt = T.veleLoose0_pt
		ele_eta = T.veleLoose0_eta
		ele_phi = T.veleLoose0_phi
		AK4_PT_0 = T.AK4Puppijet0_pt
		AK4_ETA_0 = T.AK4Puppijet0_eta
		AK4_PHI_0 = T.AK4Puppijet0_phi
		AK4_MASS_0 = T.AK4Puppijet0_mass
		AK4_PT_1 = T.AK4Puppijet1_pt
		AK4_ETA_1 = T.AK4Puppijet1_eta
		AK4_PHI_1 = T.AK4Puppijet1_phi
		AK4_MASS_1 = T.AK4Puppijet1_mass
		AK4_PT_2 = T.AK4Puppijet2_pt	
		AK4_ETA_2 = T.AK4Puppijet2_eta
		AK4_PHI_2 = T.AK4Puppijet2_phi
		AK4_MASS_2 = T.AK4Puppijet2_mass
		AK4_PT_3 = T.AK4Puppijet3_pt
		AK4_ETA_3 = T.AK4Puppijet3_eta
		AK4_PHI_3 = T.AK4Puppijet3_phi
		AK4_MASS_3 = T.AK4Puppijet3_mass
		AK4Jet_0.SetPtEtaPhiM(AK4_PT_0, AK4_ETA_0, AK4_PHI_0, AK4_MASS_0)
		AK4Jet_1.SetPtEtaPhiM(AK4_PT_1, AK4_ETA_1, AK4_PHI_1, AK4_MASS_1)
		AK4Jet_2.SetPtEtaPhiM(AK4_PT_2, AK4_ETA_2, AK4_PHI_2, AK4_MASS_2)
		AK4Jet_3.SetPtEtaPhiM(AK4_PT_3, AK4_ETA_3, AK4_PHI_3, AK4_MASS_3)
		ele_distance.SetPtEtaPhiM(ele_pt, ele_eta, ele_phi, ele_mass)
		muo_distance.SetPtEtaPhiM(muo_pt, muo_eta, muo_phi, muo_mass)
		Mt_muo_Pf = TMath.Sqrt(2.0*(muo_pt)*(PFMET)*(1.0-TMath.Cos((muo_phi-PfMET_phi))))
		Mt_ele_Pf = TMath.Sqrt(2.0*(ele_pt)*(PFMET)*(1.0-TMath.Cos((ele_phi-PfMET_phi))))
		Mt_muo_Puppi = TMath.Sqrt(2.0*(muo_pt)*(PuppiMET)*(1.0-TMath.Cos((muo_phi-PuppiMET_phi))))
		Mt_ele_Puppi = TMath.Sqrt(2.0*(ele_pt)*(PuppiMET)*(1.0-TMath.Cos((ele_phi-PuppiMET_phi))))
		Jet_0.SetPtEtaPhiM(PT_0, ETA_0, PHI_0, MASS_0)
		DELTA_R_ELE_0 = AK4Jet_0.DeltaR(ele_distance)
		DELTA_R_ELE_1 = AK4Jet_1.DeltaR(ele_distance)
		DELTA_R_ELE_2 = AK4Jet_2.DeltaR(ele_distance)
		DELTA_R_ELE_3 = AK4Jet_3.DeltaR(ele_distance)
		DELTA_R_MUO_0 = AK4Jet_0.DeltaR(muo_distance)
		DELTA_R_MUO_1 = AK4Jet_1.DeltaR(muo_distance)
		DELTA_R_MUO_2 = AK4Jet_2.DeltaR(muo_distance)
		DELTA_R_MUO_3 = AK4Jet_3.DeltaR(muo_distance)
		LOW_ANGLE_ELE_PF = TMath.ATan2(ele_pt,PFMET)
		LOW_ANGLE_MUO_PF = TMath.ATan2(muo_pt,PFMET)
		HIGH_ANGLE_ELE_PF = TMath.PiOver4() - LOW_ANGLE_ELE_PF
		HIGH_ANGLE_MUO_PF = TMath.PiOver4() - LOW_ANGLE_MUO_PF
		LOW_ANGLE_ELE_PUPPI = TMath.ATan(ele_pt/PuppiMET)
		LOW_ANGLE_MUO_PUPPI = TMath.ATan(muo_pt/PuppiMET)
		HIGH_ANGLE_ELE_PUPPI = TMath.PiOver4() - LOW_ANGLE_ELE_PUPPI
		HIGH_ANGLE_MUO_PUPPI = TMath.PiOver4() - LOW_ANGLE_MUO_PUPPI
		ATAN_PFMET_OVER_ELEPT = TMath.ATan2(ele_pt,PFMET)
		ATAN_PFMET_OVER_MUOPT = TMath.ATan2(muo_pt,PFMET)
		ATAN_PUPPET_OVER_ELEPT = TMath.ATan2(ele_pt,PuppiMET)
		ATAN_PUPPET_OVER_MUOPT = TMath.ATan2(muo_pt,PuppiMET)

 
	#Filling Histograms
#        	folder1.cd()
		Jet_Pt_0.Fill(PT_0, weight)
		Jet_Mass_0.Fill(MASS_0, weight)
		Jet_Phi_0.Fill(PHI_0, weight)
		Jet_Eta_0.Fill(ETA_0, weight)
		NJets.Fill(NJETS, weight)
		PfMet.Fill(PFMET, weight)
		PuppiMet.Fill(PuppiMET, weight)
		PfMet_phi.Fill(PfMET_phi, weight)
		PuppiMet_phi.Fill(PuppiMET_phi, weight)
		Npv.Fill(NPV, weight)
		Muo_0_pt.Fill(muo_pt, weight)
		Muo_0_eta.Fill(muo_eta, weight)
		Muo_0_phi.Fill(muo_phi, weight)
		Ele_0_pt.Fill(ele_pt, weight)
		Ele_0_eta.Fill(ele_eta, weight)
		Ele_0_phi.Fill(ele_phi, weight)
		Mt_Muo_Pf.Fill(Mt_muo_Pf, weight)
		Mt_Ele_Pf.Fill(Mt_ele_Pf, weight)
		Mt_Muo_Puppi.Fill(Mt_muo_Puppi, weight)
		Mt_Ele_Puppi.Fill(Mt_ele_Puppi, weight)
		weight_one.Fill(weight)
		weight_no_k.Fill(weight_NO_K)
		weight_k.Fill(weight_just_k)
		weight_original.Fill(weight_all)
		weight_new.Fill(weight_evt)
		weight_pu.Fill(weight_PU)
		delta_R_ele_AK4_0.Fill(DELTA_R_ELE_0, weight)
		delta_R_ele_AK4_1.Fill(DELTA_R_ELE_1, weight)
		delta_R_ele_AK4_2.Fill(DELTA_R_ELE_2, weight)
		delta_R_ele_AK4_3.Fill(DELTA_R_ELE_3, weight)
		delta_R_muo_AK4_0.Fill(DELTA_R_MUO_0, weight)
		delta_R_muo_AK4_1.Fill(DELTA_R_MUO_1, weight)
		delta_R_muo_AK4_2.Fill(DELTA_R_MUO_2, weight)
		delta_R_muo_AK4_3.Fill(DELTA_R_MUO_3, weight)
		Low_angle_elePt_over_pfmet.Fill(LOW_ANGLE_ELE_PF, weight)
		Low_angle_muoPt_over_pfmet.Fill(LOW_ANGLE_MUO_PF, weight)
		Low_angle_elePt_over_puppet.Fill(LOW_ANGLE_ELE_PUPPI, weight)
		Low_angle_muoPt_over_puppet.Fill(LOW_ANGLE_MUO_PUPPI, weight)
		High_angle_elePt_over_pfmet.Fill(HIGH_ANGLE_ELE_PF, weight)
	        High_angle_muoPt_over_pfmet.Fill(HIGH_ANGLE_MUO_PF, weight)
		High_angle_elePt_over_puppet.Fill(HIGH_ANGLE_ELE_PUPPI, weight)
		High_angle_muoPt_over_puppet.Fill(HIGH_ANGLE_MUO_PUPPI, weight)
		JetPt_vs_elePt.Fill(ele_pt, PT_0, weight)
		JetPt_vs_muoPt.Fill(muo_pt, PT_0, weight)
		elePt_vs_PfMET.Fill(PFMET, ele_pt, weight)
		muoPt_vs_PfMET.Fill(PFMET, muo_pt, weight)
		elePt_vs_PuppiMET.Fill(PuppiMET, ele_pt, weight)
		muoPt_vs_PuppiMET.Fill(PuppiMET, muo_pt, weight)
		eleMt_vs_JetPt_Pf.Fill(PT_0, Mt_ele_Pf, weight)
		muoMt_vs_JetPt_Pf.Fill(PT_0, Mt_muo_Pf, weight)
		eleMt_vs_JetPt_Puppi.Fill(PT_0, Mt_ele_Puppi, weight)
		muoMt_vs_JetPt_Puppi.Fill(PT_0, Mt_muo_Puppi, weight)
		JetPhi_vs_elePhi.Fill(ele_phi, PHI_0, weight)
		JetPhi_vs_muoPhi.Fill(muo_phi, PHI_0, weight)
		elePhi_vs_PfMETPhi.Fill(PfMET_phi, ele_phi, weight)
		muoPhi_vs_PfMETPhi.Fill(PfMET_phi, muo_phi, weight)
		elePhi_vs_PuppiMETPhi.Fill(PuppiMET_phi, ele_phi, weight)
		muoPhi_vs_PuppiMETPhi.Fill(PuppiMET_phi, muo_phi, weight)
		JetPhi_vs_PfMETPhi.Fill(PfMET_phi, PHI_0, weight)
		JetPhi_vs_PuppiMETPhi.Fill(PuppiMET_phi, PHI_0, weight)


		#Electron cuts with Pf MET
#         	folder2.cd()
		if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
			Cut_Jet_Mass_e_Pf_0.Fill(MASS_0, weight)
			Cut_Jet_Phi_e_Pf_0.Fill(PHI_0, weight)
			Cut_Jet_Eta_e_Pf_0.Fill(ETA_0, weight)
			Cut_NJets_e_Pf.Fill(NJETS, weight)
			Cut_Npv_e_Pf.Fill(NPV, weight)
      			Cut_PfMet_Phi_e.Fill(PfMET_phi, weight)
			Cut_PfMet_e.Fill(PFMET, weight)
			Cut_ele_pt_Pf.Fill(ele_pt, weight)
			Cut_ele_phi_Pf.Fill(ele_phi, weight)
			Cut_ele_eta_Pf.Fill(ele_eta, weight)
			Cut_Mt_Ele_Pf.Fill(Mt_ele_Pf, weight)
			Cut_delta_R_ele_AK4_0_pf.Fill(DELTA_R_ELE_0, weight)
			Cut_delta_R_ele_AK4_1_pf.Fill(DELTA_R_ELE_1, weight)
			Cut_delta_R_ele_AK4_2_pf.Fill(DELTA_R_ELE_2, weight)
			Cut_delta_R_ele_AK4_3_pf.Fill(DELTA_R_ELE_3, weight)
			Cut_Low_angle_elePt_over_pfmet.Fill(LOW_ANGLE_ELE_PF, weight)
			Cut_High_angle_elePt_over_pfmet.Fill(HIGH_ANGLE_ELE_PF, weight)
			CutJetPt_vs_CutelePt_Pf.Fill(ele_pt, PT_0, weight)
			CutelePt_vs_CutPfMET_WEIGHT_ONE.Fill(PFMET, ele_pt, weight)			
			CutelePt_vs_CutPfMET_WEIGHT_NO_K.Fill(PFMET, ele_pt, weight_NO_K)
			CutelePt_vs_CutPfMET_WEIGHT_JUST_K.Fill(PFMET, ele_pt, weight_just_k)
			CutelePt_vs_CutPfMET_WEIGHT_ALL.Fill(PFMET, ele_pt, weight_all)
			CutelePt_vs_CutPfMET_WEIGHT_NEW.Fill(PFMET, ele_pt, weight_evt)
			CutelePt_vs_CutPfMET_WEIGHT_PU.Fill(PFMET, ele_pt, weight_PU)
			CuteleMt_vs_CutJetPt_Pf.Fill(PT_0, Mt_ele_Pf, weight)
			CutJetPhi_vs_CutElePhi_Pf.Fill(ele_phi, PHI_0, weight)
			CutElePhi_vs_CutPfMetPhi.Fill(PfMET_phi, ele_phi, weight)
			CutJetPhi_vs_CutPfMetPhi_e.Fill(PfMET_phi, PHI_0, weight)
#			Cut_deltaR_AK4_vs_atan_pfmet_over_elePt.Fill(DELTA_R_ELE_1, ATAN_PFMET_OVER_ELEPT, weight)

			  

		#Muon cuts with Pf MET
#        	folder3.cd()
		if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
			Cut_Jet_Mass_m_Pf_0.Fill(MASS_0, weight)
			Cut_Jet_Phi_m_Pf_0.Fill(PHI_0, weight)
			Cut_Jet_Eta_m_Pf_0.Fill(ETA_0, weight)
			Cut_NJets_m_Pf.Fill(NJETS, weight)
			Cut_Npv_m_Pf.Fill(NPV, weight)
      			Cut_PfMet_Phi_m.Fill(PfMET_phi, weight)
			Cut_PfMet_m.Fill(PFMET, weight)
			Cut_muo_pt_Pf.Fill(muo_pt, weight)
			Cut_muo_phi_Pf.Fill(muo_phi, weight)
			Cut_muo_eta_Pf.Fill(muo_eta, weight)
			Cut_Mt_Muo_Pf.Fill(Mt_muo_Pf, weight)
			Cut_delta_R_muo_AK4_0_pf.Fill(DELTA_R_MUO_0, weight)
			Cut_delta_R_muo_AK4_1_pf.Fill(DELTA_R_MUO_1, weight)
			Cut_delta_R_muo_AK4_2_pf.Fill(DELTA_R_MUO_2, weight)
			Cut_delta_R_muo_AK4_3_pf.Fill(DELTA_R_MUO_3, weight)
			Cut_Low_angle_muoPt_over_pfmet.Fill(LOW_ANGLE_MUO_PF, weight)
			Cut_High_angle_muoPt_over_pfmet.Fill(HIGH_ANGLE_MUO_PF, weight)
			CutJetPt_vs_CutmuoPt_Pf.Fill(muo_pt, PT_0, weight)
			CutmuoPt_vs_CutPfMET_WEIGHT_ONE.Fill(PFMET, muo_pt, weight)
			CutmuoPt_vs_CutPfMET_WEIGHT_NO_K.Fill(PFMET, muo_pt, weight_NO_K)
			CutmuoPt_vs_CutPfMET_WEIGHT_JUST_K.Fill(PFMET, muo_pt, weight_just_k)
			CutmuoPt_vs_CutPfMET_WEIGHT_ALL.Fill(PFMET, muo_pt, weight_all)
			CutmuoPt_vs_CutPfMET_WEIGHT_NEW.Fill(PFMET, muo_pt, weight_evt)
			CutmuoPt_vs_CutPfMET_WEIGHT_PU.Fill(PFMET, muo_pt, weight_PU)
			CutmuoMt_vs_CutJetPt_Pf.Fill(PT_0, Mt_muo_Pf, weight)
			CutJetPhi_vs_CutMuoPhi_Pf.Fill(muo_phi, PHI_0, weight)
			CutMuoPhi_vs_CutPfMetPhi.Fill(PfMET_phi, muo_phi, weight)
			CutJetPhi_vs_CutPfMetPhi_m.Fill(PfMET_phi, PHI_0, weight)
#			Cut_deltaR_AK41_vs_atan_angle_pfmet_over_muoPt.Fill(DELTA_R_ELE_1, ATAN_PFMET_OVER_MUOPT, weight)


		#Electron cuts with Puppi MET
# 	        folder4.cd()
		if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
			Cut_Jet_Mass_e_Puppi_0.Fill(MASS_0, weight)
			Cut_Jet_Phi_e_Puppi_0.Fill(PHI_0, weight)
			Cut_Jet_Eta_e_Puppi_0.Fill(ETA_0, weight)
			Cut_NJets_e_Puppi.Fill(NJETS, weight)
			Cut_Npv_e_Puppi.Fill(NPV, weight)
      			Cut_PuppiMet_Phi_e.Fill(PfMET_phi, weight)
			Cut_PuppiMet_e.Fill(PFMET, weight)
			Cut_ele_pt_Puppi.Fill(ele_pt, weight)
			Cut_ele_phi_Puppi.Fill(ele_phi, weight)
			Cut_ele_eta_Puppi.Fill(ele_eta, weight)
			Cut_Mt_Ele_Puppi.Fill(Mt_ele_Puppi, weight)
			Cut_delta_R_ele_AK4_0_puppi.Fill(DELTA_R_ELE_0, weight)
			Cut_delta_R_ele_AK4_1_puppi.Fill(DELTA_R_ELE_1, weight)
			Cut_delta_R_ele_AK4_2_puppi.Fill(DELTA_R_ELE_2, weight)
			Cut_delta_R_ele_AK4_3_puppi.Fill(DELTA_R_ELE_3, weight)
			Cut_Low_angle_elePt_over_puppet.Fill(LOW_ANGLE_ELE_PUPPI, weight)
			Cut_High_angle_elePt_over_puppet.Fill(HIGH_ANGLE_ELE_PUPPI, weight)
			CutJetPt_vs_CutelePt_Puppi.Fill(ele_pt, PT_0, weight)
			CutelePt_vs_CutPuppiMET_WEIGHT_ONE.Fill(PuppiMET, ele_pt, weight)
			CutelePt_vs_CutPuppiMET_WEIGHT_NO_K.Fill(PuppiMET, ele_pt, weight_NO_K)
			CutelePt_vs_CutPuppiMET_WEIGHT_JUST_K.Fill(PuppiMET, ele_pt, weight_just_k)	
			CutelePt_vs_CutPuppiMET_WEIGHT_ALL.Fill(PuppiMET, ele_pt, weight_all)
			CutelePt_vs_CutPuppiMET_WEIGHT_NEW.Fill(PuppiMET, ele_pt, weight_evt)
			CutelePt_vs_CutPuppiMET_WEIGHT_PU.Fill(PuppiMET, ele_pt, weight_PU)
			CuteleMt_vs_CutJetPt_Puppi.Fill(PT_0, Mt_ele_Puppi, weight)
			CutJetPhi_vs_CutElePhi_Puppi.Fill(ele_phi, PHI_0, weight)
			CutElePhi_vs_CutPuppiMetPhi.Fill(PuppiMET_phi, ele_phi, weight)
			CutJetPhi_vs_CutPuppiMetPhi_e.Fill(PuppiMET_phi, PHI_0, weight)
#			Cut_deltaR_AK41_vs_atan_angle_puppet_over_elePt.Fill(DELTA_R_ELE_1, ATAN_PUPPET_OVER_ELEPT, weight)


       	#Muon cuts with Puppi MET
#        	folder5.cd()
		if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
			Cut_Jet_Mass_m_Puppi_0.Fill(MASS_0, weight)
			Cut_Jet_Phi_m_Puppi_0.Fill(PHI_0, weight)
			Cut_Jet_Eta_m_Puppi_0.Fill(ETA_0, weight)
			Cut_NJets_m_Puppi.Fill(NJETS, weight)
			Cut_Npv_m_Puppi.Fill(NPV, weight)
      			Cut_PuppiMet_Phi_m.Fill(PfMET_phi, weight)
			Cut_PuppiMet_m.Fill(PFMET, weight)
			Cut_muo_pt_Puppi.Fill(muo_pt, weight)
			Cut_muo_phi_Puppi.Fill(muo_phi, weight)
			Cut_muo_eta_Puppi.Fill(muo_eta, weight)
			Cut_Mt_Muo_Puppi.Fill(Mt_muo_Puppi, weight)
			Cut_delta_R_muo_AK4_0_puppi.Fill(DELTA_R_MUO_0, weight)
			Cut_delta_R_muo_AK4_1_puppi.Fill(DELTA_R_MUO_1, weight)
			Cut_delta_R_muo_AK4_2_puppi.Fill(DELTA_R_MUO_2, weight)
			Cut_delta_R_muo_AK4_3_puppi.Fill(DELTA_R_MUO_3, weight)
			Cut_Low_angle_muoPt_over_puppet.Fill(LOW_ANGLE_MUO_PUPPI, weight)
			Cut_High_angle_muoPt_over_puppet.Fill(HIGH_ANGLE_MUO_PUPPI, weight)
			CutJetPt_vs_CutmuoPt_Puppi.Fill(muo_pt, PT_0, weight)
			CutmuoPt_vs_CutPuppiMET_WEIGHT_ONE.Fill(PuppiMET, muo_pt, weight)
			CutmuoPt_vs_CutPuppiMET_WEIGHT_NO_K.Fill(PuppiMET, muo_pt, weight_NO_K)
			CutmuoPt_vs_CutPuppiMET_WEIGHT_JUST_K.Fill(PuppiMET, muo_pt, weight_just_k)
			CutmuoPt_vs_CutPuppiMET_WEIGHT_ALL.Fill(PuppiMET, muo_pt, weight_all)
			CutmuoPt_vs_CutPuppiMET_WEIGHT_NEW.Fill(PuppiMET, muo_pt, weight_evt)
			CutmuoPt_vs_CutPuppiMET_WEIGHT_PU.Fill(PuppiMET, muo_pt, weight_PU)
			CutmuoMt_vs_CutJetPt_Puppi.Fill(PT_0, Mt_muo_Puppi, weight)
			CutJetPhi_vs_CutMuoPhi_Puppi.Fill(muo_phi, PHI_0, weight)
			CutMuoPhi_vs_CutPuppiMetPhi.Fill(PuppiMET_phi, muo_phi, weight)
			CutJetPhi_vs_CutPuppiMetPhi_m.Fill(PuppiMET_phi, PHI_0, weight)
#			Cut_deltaR_AK41_vs_atan_angle_puppet_over_muoPt.Fill(DELTA_R_ELE_1, ATAN_PUPPET_OVER_MUOPT, weight)
 


		if DELTA_R_ELE_0 < DELTA_R_ELE_1 < DELTA_R_ELE_2 < DELTA_R_ELE_3:
			deltaR_AK40_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_0, ATAN_PFMET_OVER_ELEPT, weight)
			deltaR_AK40_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_0, ATAN_PUPPET_OVER_ELEPT, weight)
			
			DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_0, ATAN_PFMET_OVER_ELEPT, weight)
			DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_0, ATAN_PUPPET_OVER_ELEPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK40_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_0, ATAN_PFMET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_0, ATAN_PFMET_OVER_ELEPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK40_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_0, ATAN_PUPPET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_0, ATAN_PUPPET_OVER_ELEPT, weight)




		if DELTA_R_ELE_1 < DELTA_R_ELE_2 < DELTA_R_ELE_3 < DELTA_R_ELE_0:
			deltaR_AK41_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_1, ATAN_PFMET_OVER_ELEPT, weight)
			deltaR_AK41_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_1, ATAN_PUPPET_OVER_ELEPT, weight)

			DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_1, ATAN_PFMET_OVER_ELEPT, weight)
			DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_1, ATAN_PUPPET_OVER_ELEPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK41_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_1, ATAN_PFMET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_1, ATAN_PFMET_OVER_ELEPT, weight)

			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK41_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_1, ATAN_PUPPET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_1, ATAN_PUPPET_OVER_ELEPT, weight)


 

		if DELTA_R_ELE_2 < DELTA_R_ELE_3 < DELTA_R_ELE_0 < DELTA_R_ELE_1:
			deltaR_AK42_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_2, ATAN_PFMET_OVER_ELEPT, weight)
			deltaR_AK42_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_2, ATAN_PUPPET_OVER_ELEPT, weight)

			DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_2, ATAN_PFMET_OVER_ELEPT, weight)
			DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_2, ATAN_PUPPET_OVER_ELEPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK42_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_2, ATAN_PFMET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_2, ATAN_PFMET_OVER_ELEPT, weight)

			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK42_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_2, ATAN_PUPPET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_2, ATAN_PUPPET_OVER_ELEPT, weight)






		if DELTA_R_ELE_3 < DELTA_R_ELE_0 < DELTA_R_ELE_1 < DELTA_R_ELE_2:
			deltaR_AK43_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_3, ATAN_PFMET_OVER_ELEPT, weight)
			deltaR_AK43_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_3, ATAN_PUPPET_OVER_ELEPT, weight)

			DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_3, ATAN_PFMET_OVER_ELEPT, weight)
			DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_3, ATAN_PFMET_OVER_ELEPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK43_vs_atan_angle_elePt_over_pfmet.Fill(DELTA_R_ELE_3, ATAN_PFMET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_pf.Fill(DELTA_R_ELE_3, ATAN_PFMET_OVER_ELEPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (ele_pt > muo_pt) and (abs(ele_eta) < 2.5):
				Cut_deltaR_AK43_vs_atan_angle_elePt_over_puppet.Fill(DELTA_R_ELE_3, ATAN_PUPPET_OVER_ELEPT, weight)

				Cut_DeltaR_AK4_vs_atan_elePt_over_puppi.Fill(DELTA_R_ELE_3, ATAN_PUPPET_OVER_ELEPT, weight)






                if DELTA_R_MUO_0 < DELTA_R_MUO_1 < DELTA_R_MUO_2 < DELTA_R_MUO_3:
			deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_0, ATAN_PFMET_OVER_MUOPT, weight)
			deltaR_AK40_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_0, ATAN_PUPPET_OVER_MUOPT, weight)


			DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_0, ATAN_PFMET_OVER_MUOPT, weight)
			DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_0, ATAN_PUPPET_OVER_MUOPT, weight)



			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK40_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_0, ATAN_PFMET_OVER_MUOPT, weight)

				Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_0, ATAN_PFMET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK40_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_0, ATAN_PUPPET_OVER_MUOPT, weight)


				Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_0, ATAN_PUPPET_OVER_MUOPT, weight)


			

		if DELTA_R_MUO_1 < DELTA_R_MUO_2 < DELTA_R_MUO_3 < DELTA_R_MUO_0:
			deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_1, ATAN_PFMET_OVER_MUOPT, weight)
			deltaR_AK41_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_1, ATAN_PUPPET_OVER_MUOPT, weight)

			DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_1, ATAN_PFMET_OVER_MUOPT, weight)
			DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_1, ATAN_PUPPET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK41_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_1, ATAN_PFMET_OVER_MUOPT, weight)	

				Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_1, ATAN_PFMET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK41_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_1, ATAN_PUPPET_OVER_MUOPT, weight)


				Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_1, ATAN_PUPPET_OVER_MUOPT, weight)




		if DELTA_R_MUO_2 < DELTA_R_MUO_3 < DELTA_R_MUO_0 < DELTA_R_MUO_1:
			deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_2, ATAN_PFMET_OVER_MUOPT, weight)
			deltaR_AK42_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_2, ATAN_PUPPET_OVER_MUOPT, weight)

			DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_2, ATAN_PFMET_OVER_MUOPT, weight)
			DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_2, ATAN_PUPPET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK42_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_2, ATAN_PFMET_OVER_MUOPT, weight)

				Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_2, ATAN_PFMET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (muo_pt > muo_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK42_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_2, ATAN_PUPPET_OVER_MUOPT, weight)

				Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_2, ATAN_PUPPET_OVER_MUOPT, weight)






		if DELTA_R_MUO_3 < DELTA_R_MUO_1 < DELTA_R_MUO_2 < DELTA_R_MUO_0:
			deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_3, ATAN_PFMET_OVER_MUOPT, weight)
			deltaR_AK43_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_3, ATAN_PUPPET_OVER_MUOPT, weight)

			DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_3, ATAN_PFMET_OVER_MUOPT, weight)
			DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_3, ATAN_PUPPET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PFMET > 50.0) and (muo_pt > 50.0) and (muo_pt > ele_pt) and (abs(muo_eta) < 2.5):
				Cut_deltaR_AK43_vs_atan_angle_muoPt_over_pfmet.Fill(DELTA_R_MUO_3, ATAN_PFMET_OVER_MUOPT, weight)

				Cut_DeltaR_AK4_vs_atan_muoPt_over_pf.Fill(DELTA_R_MUO_3, ATAN_PFMET_OVER_MUOPT, weight)


			if (PT_0 > 200.0) and (abs(ETA_0) < 2.5) and (PuppiMET > 50.0) and (ele_pt > 50.0) and (muo_pt > muo_pt) and (abs(muo_eta) < 2.5):
              			Cut_deltaR_AK43_vs_atan_angle_muoPt_over_puppet.Fill(DELTA_R_MUO_3, ATAN_PUPPET_OVER_MUOPT, weight)


				Cut_DeltaR_AK4_vs_atan_muoPt_over_puppi.Fill(DELTA_R_MUO_3, ATAN_PUPPET_OVER_MUOPT, weight)

########################################################################################################################################################################

	print " "
	print " -------------------- Creating Plots"


#	folder1.cd()
#	folder1.Write()
#	folder1.Close()
#	folder2.cd()
#	folder2.Write()
#	folder2.Close()
#	folder3.cd()
#	folder3.Write()
#	folder3.Close()
#	folder4.cd()
#	folder4.Write()
#	folder4.Close()
#	folder5.cd()
#	folder5.Write()
#	folder5.Close()

	outfile.cd()
	outfile.Write()
	outfile.Close()


from optparse import OptionParser


parser = OptionParser()

parser.add_option('-n', '--name', metavar='NAME', type='string', dest='n', help="The name of the output file, minus the .root.")
parser.add_option('-f', '--file', metavar='FILES', type='string', dest='files', help="Location of the ntuples to run over.")
	
(options, args) = parser.parse_args()

MakeKinPlots(options.files, options.n)	
