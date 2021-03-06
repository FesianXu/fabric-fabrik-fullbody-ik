import json
from maya import cmds
import FabricEngine.Core
import textwrap


def splice(operator, command, *args, **kwargs):
    json.dumps(kwargs)
    return cmds.fabricSplice(command, operator, json.dumps(kwargs), *args)


def set_kl(operator, op_name, code):
    #splice(operator, "addKLOperator", opName=op_name)
    splice(operator, "setKLOperatorCode", code, opName=op_name)


cmds.spaceLocator(name="null")
cmds.move(7.21095660746,      14.9754557972,  -0.257095710115)
cmds.spaceLocator(name="null") 
cmds.move(-7.21079536001,     14.9612588443,  -0.2533093422)
cmds.spaceLocator(name="null") 
cmds.move(1.5139886508,       0.913547291364, -0.29962025889)
cmds.spaceLocator(name="null") 
cmds.move(-1.5139886508,      0.913547291364, -0.299620258891)
cmds.spaceLocator(name="null")


klCode = textwrap.dedent("""
require Math;
require Characters;
require FABRIK;

require InlineDrawing;

operator initCharacter( io Skeleton skeleton, io DrawingHandle handle, io FFBIKGraph fbg, in Mat44 ik_handles[], io FABRIKResolver resolver, Vec3 result ) {

  //////////////////////////////////
  // Generate a chain of bones with a random shape.

  //Skeleton skeleton = Skeleton();

    report( "hello" );

    if( skeleton.bones.size() == 0 ) {
        Bone bones[];
        bones.resize(0);
        report( "init skeleton" );
        skeleton = Skeleton("", bones);
        skeleton.addBone("root", "", Xfo() );

        skeleton.addBone("bicep_Lft_Bone",     "arm_Lft_Chn",        Xfo( Vec3(2.02090957899,      14.7792167213,  -0.848431284415),  Quat(-0.927651013653,  0.00630325953678, -0.027684353318,   0.372367348689)),   2.63653395236);
        skeleton.addBone("forearm_Lft_Bone",   "bicep_Lft_Bone",     Xfo( Vec3(4.65319262393,      14.6940251715,  -0.725387986754),  Quat(-0.92390072814,   -0.0835678093192, -0.0636173639348,  0.367935723727)),   2.61546505404);
        skeleton.addBone("hand_Lft_Bone",      "hand_Lft_Chn",       Xfo( Vec3(7.21095660746,      14.9754557972,  -0.257095710115),  Quat(-0.463212761098,  -0.137349843791,  -0.0866854577564,  0.871237390027)),   1.2025080972);
        skeleton.addBone("bicep_Rgt_Bone",     "arm_Rgt_Chn",        Xfo( Vec3(-2.02090953805,     14.7792173752,  -0.848431356336),  Quat(-0.0283859377662, 0.373006195942,   -0.927363315646,   0.00760901569113)), 2.63653395236);
        skeleton.addBone("forearm_Rgt_Bone",   "bicep_Rgt_Bone",     Xfo( Vec3(-4.65288936006,     14.6861769781,  -0.724588782911),  Quat(0.0645539024774,  -0.368472763374,  0.9237013718,      0.082682477348)),   2.61546505404);
        skeleton.addBone("hand_Rgt_Bone",      "hand_Rgt_Chn",       Xfo( Vec3(-7.21079536001,     14.9612588443,  -0.2533093422),    Quat(0.0806220903861,  -0.85118646362,   0.503458278753,    0.124544948704)),   1.2025080972);
        skeleton.addBone("thorax1_Mid_Bone",   "thorax_Mid_Chn",     Xfo( Vec3(-3.9534678086e-12,  11.9882806957,  -0.256887428953),  Quat(-0.531701542117,  -0.466147476783,  0.531701542116,    0.466147476783)),   3.37078229482);
        skeleton.addBone("scapula1_Rgt_Bone",  "scapula_Rgt_Chn",    Xfo( Vec3(-0.0134124436876,   14.603458196,   -1.40226202867),   Quat(0.010630822139,   0.686924770797,   0.723884722442,    0.0633423515584)),  0.729220886867);
        skeleton.addBone("scapula2_Rgt_Bone",  "scapula1_Rgt_Bone",  Xfo( Vec3(-0.73661686755,     14.6809818663,  -1.45449749259),   Quat(-0.184336363305,  -0.661814747703,  -0.716311850831,   0.122142037173)),   1.42350765373);
        skeleton.addBone("clavicle_Rgt_Bone",  "clavicle_Rgt_Chn",   Xfo( Vec3(-0.279588742967,    14.8112134967,  0.433742071629),   Quat(0.311993690914,   0.00286614206865, -0.950039763095,   0.00872757690571)), 2.16268133634);
        skeleton.addBone("scapula1_Lft_Bone",  "scapula_Lft_Chn",    Xfo( Vec3(0.0134124436866,    14.603458196,   -1.40226202867),   Quat(0.723884761637,   0.0633422287663,  0.0106307343362,   0.686924742175)),   0.729220886867);
        skeleton.addBone("scapula2_Lft_Bone",  "scapula1_Lft_Bone",  Xfo( Vec3(0.736616892959,     14.6809816519,  -1.45449745902),   Quat(0.716311858483,   -0.122142160916,  0.184336266521,    0.661814743542)),   1.42350765373);
        skeleton.addBone("clavicle_Lft_Bone",  "clavicle_Lft_Chn",   Xfo( Vec3(0.279588742963,     14.8112134967,  0.43374207163),    Quat(0.00286620038887, 0.311993670761,   -0.00872775510217, 0.9500397679)),     2.16268133634);
        skeleton.addBone("cervical1_Mid_Bone", "cervical_Mid_Chn",   Xfo( Vec3(8.92154308481e-14,  15.3300922258,  -0.698305257947),  Quat(-0.436396161401,  -0.556379717742,  0.436396161401,    0.556379717741)),   0.45995653989);
        skeleton.addBone("cervical2_Mid_Bone", "cervical1_Mid_Bone", Xfo( Vec3(-3.66097987527e-14, 15.7768056475,  -0.588728173426),  Quat(-0.437297900241,  -0.55567125753,   0.437297900239,    0.555671257532)),   0.459921714248);
        skeleton.addBone("cervical3_Mid_Bone", "cervical2_Mid_Bone", Xfo( Vec3(1.78695196739e-12,  16.2238382841,  -0.480608771552),  Quat(-0.46426997124,   -0.533341723293,  0.464269971242,    0.533341723291)),   0.459927437779);
        skeleton.addBone("lumbar1_Mid_Bone",   "lumbar_Mid_Chn",     Xfo( Vec3(4.93247247365e-15,  10.2323828082,  -0.128196598423),  Quat(-0.481105981204,  -0.518205591295,  0.481105981205,    0.518205591294)),   0.591509348722);
        skeleton.addBone("lumbar2_Mid_Bone",   "lumbar1_Mid_Bone",   Xfo( Vec3(-6.28396045942e-13, 10.8222638723,  -0.0843372807799), Quat(-0.517883088037,  -0.481453120382,  0.517883088038,    0.48145312038)),    0.590862195512);
        skeleton.addBone("lumbar3_Mid_Bone",   "lumbar2_Mid_Bone",   Xfo( Vec3(-2.06428996055e-12, 11.4115577511,  -0.127358885776),  Quat(-0.552072274071,  -0.441832778552,  0.552072274072,    0.44183277855)),    0.591089670265);
        skeleton.addBone("head_Mid_Bone",      "head_Mid_Chn",       Xfo( Vec3(-2.31829712283e-13, 16.6824188064,  -0.416801311344),  Quat(0.542376619824,   0.453682270172,   0.542376619824,    0.453682270172)),   1.74543107082);
        skeleton.addBone("thigh_Rgt_Bone",     "leg_Rgt_Chn",        Xfo( Vec3(-1.09189253003,     9.63678764269,  -0.153153425243),  Quat(-0.403046495643,  0.405149026325,   -0.60960993169,    0.549348268408)),   4.28213777723);
        skeleton.addBone("shin_Rgt_Bone",      "thigh_Rgt_Bone",     Xfo( Vec3(-1.39823668671,     5.3702192418,   0.0449659362325),  Quat(-0.375533924058,  0.430774283197,   -0.572168595084,   0.58824390147)),    4.47147213308);
        skeleton.addBone("foot_Rgt_Bone",      "foot_Rgt_Chn",       Xfo( Vec3(-1.5139886508,      0.913547291364, -0.299620258891),  Quat(0.171685501935,   -0.79204168527,   -0.124103767301,   0.572531494472)),   1.71057902684);
        skeleton.addBone("toes_Rgt_Bone",      "foot_Rgt_Bone",      Xfo( Vec3(-2.00229661668,     0.205246500659, 1.17887422112),    Quat(0.0423869490891,  -0.798690207548,  -0.0318107251374,  0.599404184737)),   0.895697040854);
        skeleton.addBone("thigh_Lft_Bone",     "leg_Lft_Chn",        Xfo( Vec3(1.09189253003,      9.63678764269,  -0.153153425243),  Quat(-0.609609934903,  0.549348271201,   -0.403046491254,   0.405149022069)),   4.28213777723);
        skeleton.addBone("shin_Lft_Bone",      "thigh_Lft_Bone",     Xfo( Vec3(1.39823669072,      5.37021924202,  0.0449659347465),  Quat(-0.572168598107,  0.588243904469,   -0.375533919959,   0.430774278661)),   4.47147213308);
        skeleton.addBone("foot_Lft_Bone",      "foot_Lft_Chn",       Xfo( Vec3(1.5139886508,       0.913547291364, -0.29962025889),   Quat(0.140843108114,   -0.568364962503,  -0.194153520233,   0.787038054275)),   1.71057902684);
        skeleton.addBone("toes_Lft_Bone",      "foot_Lft_Bone",      Xfo( Vec3(1.99043855347,      0.116908412472, 1.13719656798),    Quat(0.00207783260288, -0.600355063244,  -0.00276785696612, 0.799726090369)),   0.895697040854);


        fbg = FFBIKGraph( skeleton );
        // upper body triangle
        fbg.addEdge( "lumbar2_Mid_Bone", "bicep_Lft_Bone" );
        fbg.addEdge( "lumbar2_Mid_Bone", "bicep_Rgt_Bone" );
        fbg.addEdge( "bicep_Lft_Bone",   "bicep_Rgt_Bone" );
        //fbg.addEdge( "bicep_Lft_Bone",   "cervical1_Mid_Bone" );
        //fbg.addEdge( "bicep_Rgt_Bone",   "cervical1_Mid_Bone" );
        // lower body 
        fbg.addEdge( "lumbar2_Mid_Bone", "thigh_Lft_Bone" );
        fbg.addEdge( "lumbar2_Mid_Bone", "thigh_Rgt_Bone" );
        fbg.addEdge( "thigh_Lft_Bone",   "thigh_Rgt_Bone" );
        // leg
        fbg.addEdge( "thigh_Lft_Bone",   "shin_Lft_Bone" );
        fbg.addEdge( "shin_Lft_Bone",    "foot_Lft_Bone" );
        fbg.addEdge( "thigh_Rgt_Bone",   "shin_Rgt_Bone" );
        fbg.addEdge( "shin_Rgt_Bone",    "foot_Rgt_Bone" );
        // arm
        fbg.addEdge( "bicep_Lft_Bone",   "forearm_Lft_Bone" );
        fbg.addEdge( "forearm_Lft_Bone", "hand_Lft_Bone" );
        fbg.addEdge( "bicep_Rgt_Bone",   "forearm_Rgt_Bone" );
        fbg.addEdge( "forearm_Rgt_Bone", "hand_Rgt_Bone" );
        //fbg.addEdge( "lumbar2_Mid_Bone", "cervical1_Mid_Bone" );
        fbg.finalize();


        FFBIKPose pose = FFBIKPose(skeleton);

        for (k, v in fbg.nodes ){
            report( k + ":    "+ skeleton.getBone( k ).name );
        }


        String x[];
        addArmSolver( resolver, fbg, skeleton, handle, "lumbar2_Mid_Bone", "bicep_Lft_Bone", "forearm_Lft_Bone", "hand_Lft_Bone");
        addArmSolver( resolver, fbg, skeleton, handle, "lumbar2_Mid_Bone", "bicep_Rgt_Bone", "forearm_Rgt_Bone", "hand_Rgt_Bone");
        addLegSolver( resolver, fbg, skeleton, handle, "lumbar2_Mid_Bone", "thigh_Lft_Bone", "shin_Lft_Bone", "foot_Lft_Bone");
        addLegSolver( resolver, fbg, skeleton, handle, "lumbar2_Mid_Bone", "thigh_Rgt_Bone", "shin_Rgt_Bone", "foot_Rgt_Bone");

        x.resize(0);
        x.push( "lumbar2_Mid_Bone" );
        x.push( "bicep_Lft_Bone" );
        x.push( "bicep_Rgt_Bone" );
        resolver.addSolver( FABRIKCloseLoopSolver( skeleton, fbg, handle, x ) );

        x.resize(0);
        x.push( "lumbar2_Mid_Bone" );
        x.push( "thigh_Lft_Bone" );
        x.push( "thigh_Rgt_Bone" );
        resolver.addSolver( FABRIKCloseLoopSolver( skeleton, fbg, handle, x ) );

        //x.resize(0);
        //x.push( "lumbar2_Mid_Bone" );
        //x.push( "cervical1_Mid_Bone" );
        //resolver.addSolver( FABRIKCloseLoopSolver( skeleton, fbg, handle, x ) );
    }  
    FFBIKPose pose = FFBIKPose(skeleton);
    resolver.solve( IPose( pose ), ik_handles );
    fbg.drawEdges( ISkeleton(skeleton), IPose(pose), handle );
    fbg.drawNodes( ISkeleton(skeleton), IPose(pose), handle );
    //drawSkeleton( ISkeleton(skeleton), IPose(pose), handle.getRootTransform() );

}
""")
# [Splice] DGGraph 'MayaGraph' constructed new DGNode 'DGNode'. # 

node = cmds.createNode('spliceMayaNode', name="sampleFFFBIK")
splice(node, "addIOPort", portName="skeleton",    dataType="Skeleton",       extension="Characters", addSpliceMayaAttr=True)
splice(node, "addIOPort", portName="handle",      dataType="DrawingHandle",   extension="InlineDrawing", addSpliceMayaAttr=True)
splice(node, "addIOPort", portName="fbg",         dataType="FFBIKGraph",      extension="FABRIK", addSpliceMayaAttr=True)
splice(node, "addIOPort", portName="resolver",    dataType="FABRIKResolver", extension="FABRIK", addSpliceMayaAttr=True)
splice(node, "addInputPort",    portName="ik_handles", dataType="Mat44[]", arrayType="Array (Multi)", addSpliceMayaAttr=False, addMayaAttr=True, tragets="null.xformMatrix,null2.xformMatrix")
splice(node, "addOutputPort", portName="result",    dataType="Vec3", addMayaAttr=True)
splice(node, 'addKLOperator', portMode= "io", portName="result",     targets="null.kine.global", opName="initCharacter")
set_kl(node, "initCharacter", klCode)

cmds.connectAttr("null.xformMatrix", "sampleFFFBIK.ik_handles[0]")
cmds.connectAttr("null1.xformMatrix", "sampleFFFBIK.ik_handles[1]")
cmds.connectAttr("null2.xformMatrix", "sampleFFFBIK.ik_handles[2]")
cmds.connectAttr("null3.xformMatrix", "sampleFFFBIK.ik_handles[3]")
cmds.connectAttr("sampleFFFBIK.result", "null4.scale")

#cmds.setAttr(node+'.dummy', 12)

